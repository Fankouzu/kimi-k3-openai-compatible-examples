# Quickstart

This guide shows the shortest path to test Kimi K3 through an OpenAI-compatible API endpoint.

`lizh.ai` is an independent API gateway. It is not the official Moonshot AI or Kimi website. Use the official Kimi documentation for provider-specific model behavior, and use this guide for OpenAI-compatible setup examples.

## Configuration

Use these values in any OpenAI-compatible client:

```text
Base URL: https://lizh.ai/v1
Model ID: kimi-k3
API Key: your lizh.ai API key
```

Create an API key at [https://lizh.ai/keys](https://lizh.ai/keys).

Check current model availability and pricing at [https://lizh.ai/pricing](https://lizh.ai/pricing).

## First request

Set your API key:

```bash
export LIZH_API_KEY="your_lizh_api_key"
```

Then send a small test request:

```bash
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
```

If this works, your endpoint, key, and model name are correct.

## Next

- Use [Python](python.md) for backend experiments.
- Use [Node.js](nodejs.md) for web service integration.
- Use [Cursor](cursor.md), [Hermes](hermes.md), or [OpenClaw](openclaw.md) for AI coding workflows.
