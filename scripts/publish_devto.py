#!/usr/bin/env python3
"""Publish a Markdown article to Dev.to as a draft by default."""

from __future__ import annotations

import argparse
import getpass
import json
import os
from pathlib import Path
from typing import Any
from urllib import request
from urllib.error import HTTPError


API_URL = "https://dev.to/api/articles"


def parse_frontmatter(markdown: str) -> tuple[dict[str, Any], str]:
    if not markdown.startswith("---\n"):
        return {}, markdown

    end = markdown.find("\n---\n", 4)
    if end == -1:
        return {}, markdown

    raw = markdown[4:end]
    body = markdown[end + len("\n---\n") :]
    meta: dict[str, Any] = {}

    for line in raw.splitlines():
        if not line.strip() or ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1]
        elif value.lower() == "true":
            meta[key.strip()] = True
            continue
        elif value.lower() == "false":
            meta[key.strip()] = False
            continue
        meta[key.strip()] = value

    return meta, body.lstrip()


def normalize_tags(value: Any) -> str:
    if isinstance(value, list):
        return ",".join(str(tag).strip() for tag in value if str(tag).strip())
    if isinstance(value, str):
        return ",".join(tag.strip() for tag in value.split(",") if tag.strip())
    return ""


def build_payload(path: Path, publish: bool) -> dict[str, Any]:
    meta, body = parse_frontmatter(path.read_text(encoding="utf-8"))
    title = str(meta.get("title") or "").strip()
    if not title:
        raise SystemExit("Article frontmatter must include a title.")

    article = {
        "title": title,
        "published": publish,
        "body_markdown": body,
        "tags": normalize_tags(meta.get("tags")),
    }

    for field in ("description", "canonical_url"):
        if meta.get(field):
            article[field] = meta[field]

    return {"article": article}


def post_article(api_key: str, payload: dict[str, Any]) -> dict[str, Any]:
    data = json.dumps(payload).encode("utf-8")
    req = request.Request(
        API_URL,
        data=data,
        method="POST",
        headers={
            "api-key": api_key,
            "Accept": "application/vnd.forem.api-v1+json",
            "Content-Type": "application/json",
            "User-Agent": "lizh-ai-devto-publisher/1.0",
        },
    )

    try:
        with request.urlopen(req, timeout=45) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except HTTPError as error:
        body = error.read().decode("utf-8", errors="replace")
        raise SystemExit(f"Dev.to API error {error.code}: {body}") from error


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("markdown", type=Path)
    parser.add_argument("--publish", action="store_true", help="Publish publicly instead of creating a draft.")
    parser.add_argument("--dry-run", action="store_true", help="Print the API payload without sending it.")
    args = parser.parse_args()

    payload = build_payload(args.markdown, publish=args.publish)
    if args.dry_run:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return

    api_key = os.environ.get("DEVTO_API_KEY") or getpass.getpass("DEVTO_API_KEY: ")
    if not api_key:
        raise SystemExit("Missing DEVTO_API_KEY.")

    result = post_article(api_key, payload)
    print(
        json.dumps(
            {
                "id": result.get("id"),
                "title": result.get("title"),
                "published": result.get("published"),
                "url": result.get("url"),
                "path": result.get("path"),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
