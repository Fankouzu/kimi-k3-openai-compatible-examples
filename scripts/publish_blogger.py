#!/usr/bin/env python3
"""Publish or update the Blogger Kimi K3 article."""

from __future__ import annotations

import argparse
import json
import os
import secrets
import sys
import time
import urllib.parse
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.error import HTTPError


SCOPES = ["https://www.googleapis.com/auth/blogger"]
TOKEN_PATH = Path.home() / ".codex" / "credentials" / "lizh-google-blogger-token.json"
CLIENT_SECRET_CANDIDATES = [
    Path.home() / "Downloads" / "client_secret.json",
    Path.home() / "Downloads" / "client_secret_364345540218-g4u6ds2hhp2a3hfac0sga6o4rrnjbo8k.apps.googleusercontent.com.json",
]


def read_client_config(path: Path | None) -> dict:
    candidates = [path] if path else CLIENT_SECRET_CANDIDATES
    for candidate in candidates:
        if candidate and candidate.exists():
            data = json.loads(candidate.read_text())
            return data.get("installed") or data.get("web") or data
    raise SystemExit("No Google OAuth client_secret JSON found.")


def http_json(url: str, *, method: str = "GET", token: str | None = None, body: dict | None = None) -> dict:
    data = json.dumps(body).encode("utf-8") if body is not None else None
    headers = {"Accept": "application/json"}
    if body is not None:
        headers["Content-Type"] = "application/json"
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except HTTPError as error:
        detail = error.read().decode("utf-8", errors="replace")
        raise SystemExit(f"HTTP {error.code}: {detail}") from error


def token_request(client: dict, params: dict) -> dict:
    token_uri = client.get("token_uri", "https://oauth2.googleapis.com/token")
    data = urllib.parse.urlencode(params).encode("utf-8")
    req = urllib.request.Request(token_uri, data=data, method="POST", headers={"Content-Type": "application/x-www-form-urlencoded"})
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except HTTPError as error:
        detail = error.read().decode("utf-8", errors="replace")
        raise SystemExit(f"OAuth token error {error.code}: {detail}") from error


def save_token(token: dict) -> None:
    TOKEN_PATH.parent.mkdir(parents=True, exist_ok=True)
    token["saved_at"] = int(time.time())
    if "expires_in" in token:
        token["expires_at"] = int(time.time()) + int(token["expires_in"]) - 60
    TOKEN_PATH.write_text(json.dumps(token, indent=2), encoding="utf-8")
    TOKEN_PATH.chmod(0o600)


def refresh_token_if_needed(client: dict, token: dict) -> dict:
    if token.get("access_token") and int(token.get("expires_at", 0)) > int(time.time()):
        return token
    if not token.get("refresh_token"):
        raise SystemExit("Blogger token has no refresh_token. Run auth again.")
    refreshed = token_request(client, {
        "client_id": client["client_id"],
        "client_secret": client["client_secret"],
        "refresh_token": token["refresh_token"],
        "grant_type": "refresh_token",
    })
    refreshed["refresh_token"] = token["refresh_token"]
    refreshed["scope"] = token.get("scope", " ".join(SCOPES))
    save_token(refreshed)
    return refreshed


def run_auth(client: dict, port: int) -> None:
    state = secrets.token_urlsafe(24)
    redirect_uri = f"http://127.0.0.1:{port}/"
    auth_url = client.get("auth_uri", "https://accounts.google.com/o/oauth2/auth") + "?" + urllib.parse.urlencode({
        "client_id": client["client_id"],
        "redirect_uri": redirect_uri,
        "response_type": "code",
        "scope": " ".join(SCOPES),
        "access_type": "offline",
        "prompt": "consent",
        "state": state,
    })

    result: dict[str, str] = {}

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *_args):
            return

        def do_GET(self):
            parsed = urllib.parse.urlparse(self.path)
            query = urllib.parse.parse_qs(parsed.query)
            if query.get("state", [""])[0] != state:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"Invalid state")
                return
            result["code"] = query.get("code", [""])[0]
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Blogger authorization received. You can return to Codex.")

    print(auth_url, flush=True)
    server = HTTPServer(("127.0.0.1", port), Handler)
    server.handle_request()
    if not result.get("code"):
        raise SystemExit("No OAuth code received.")
    token = token_request(client, {
        "client_id": client["client_id"],
        "client_secret": client["client_secret"],
        "code": result["code"],
        "redirect_uri": redirect_uri,
        "grant_type": "authorization_code",
    })
    save_token(token)
    print(json.dumps({"ok": True, "token_saved": str(TOKEN_PATH), "scope": token.get("scope")}, indent=2))


def get_token(client: dict) -> dict:
    if not TOKEN_PATH.exists():
        raise SystemExit("Missing Blogger OAuth token. Run: scripts/publish_blogger.py auth")
    return refresh_token_if_needed(client, json.loads(TOKEN_PATH.read_text()))


def list_blogs(token: str) -> dict:
    return http_json("https://www.googleapis.com/blogger/v3/users/self/blogs", token=token)


def publish_post(token: str, blog_id: str, title: str, content: str, labels: list[str], publish: bool) -> dict:
    url = f"https://www.googleapis.com/blogger/v3/blogs/{blog_id}/posts/?isDraft={'false' if publish else 'true'}"
    return http_json(url, method="POST", token=token, body={
        "kind": "blogger#post",
        "title": title,
        "content": content,
        "labels": labels,
    })


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["auth", "blogs", "publish"])
    parser.add_argument("--client-secret", type=Path)
    parser.add_argument("--port", type=int, default=57531)
    parser.add_argument("--blog-id")
    parser.add_argument("--html", type=Path, default=Path("content/blogger-kimi-k3-python-cursor-openai-compatible.html"))
    parser.add_argument("--publish", action="store_true", help="Publish publicly. Default creates a draft.")
    args = parser.parse_args()

    client = read_client_config(args.client_secret)
    if args.command == "auth":
        run_auth(client, args.port)
        return

    token_data = get_token(client)
    access_token = token_data["access_token"]
    if args.command == "blogs":
        blogs = list_blogs(access_token).get("items", [])
        print(json.dumps([
            {"id": blog.get("id"), "name": blog.get("name"), "url": blog.get("url")}
            for blog in blogs
        ], ensure_ascii=False, indent=2))
        return

    if not args.blog_id:
        raise SystemExit("--blog-id is required for publish")
    post = publish_post(
        access_token,
        args.blog_id,
        "How to use Kimi K3 API with Python, Cursor, and OpenAI-compatible tools",
        args.html.read_text(encoding="utf-8"),
        ["Kimi K3", "AI API", "OpenAI-compatible", "Python", "Cursor"],
        publish=args.publish,
    )
    print(json.dumps({
        "id": post.get("id"),
        "title": post.get("title"),
        "url": post.get("url"),
        "status": post.get("status"),
        "published": post.get("published"),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
