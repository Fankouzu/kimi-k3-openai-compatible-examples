#!/usr/bin/env bash
set -euo pipefail

if [[ -z "${LIZH_API_KEY:-}" ]]; then
  echo "Set LIZH_API_KEY before running this script." >&2
  exit 1
fi

curl https://lizh.ai/v1/chat/completions \
  -H "Authorization: Bearer ${LIZH_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "kimi-k3",
    "messages": [
      {
        "role": "user",
        "content": "Write a short Kimi K3 API test plan."
      }
    ],
    "max_tokens": 500
  }'
