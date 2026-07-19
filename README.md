# Kimi K3 OpenAI-Compatible API Examples

Practical examples for calling `kimi-k3` with an OpenAI-compatible API endpoint.

This repository shows the minimum setup for Python, cURL, Node.js, Cursor, Hermes, and OpenClaw. It uses [lizh.ai](https://lizh.ai/) as the API gateway so you can test Kimi K3 with the same API shape used by many OpenAI-compatible tools.

> lizh.ai is an independent OpenAI-compatible API gateway. It is not the official Moonshot AI or Kimi API website.

## Quick Start

1. Create or sign in to your lizh.ai account.
2. Create an API key at [https://lizh.ai/keys](https://lizh.ai/keys).
3. Check the current `kimi-k3` model price at [https://lizh.ai/pricing](https://lizh.ai/pricing).
4. Set your environment variable:

```bash
export LIZH_API_KEY="your_lizh_api_key"
```

5. Use these values in any OpenAI-compatible client:

```text
Base URL: https://lizh.ai/v1
Model ID: kimi-k3
API Key: $LIZH_API_KEY
```

## Python

Install the OpenAI SDK:

```bash
pip install openai
```

Run:

```bash
python examples/python_chat.py
```

## cURL

```bash
bash examples/curl_chat.sh
```

## Node.js

```bash
npm install openai
node examples/node_chat.mjs
```

## Cursor

Use an OpenAI-compatible provider:

```text
Provider: OpenAI-compatible
Base URL: https://lizh.ai/v1
API Key: your lizh.ai API key
Model: kimi-k3
```

Detailed guide: [Kimi K3 in Cursor](https://shop.lizh.ai/blogs/kimi-k3-api/kimi-k3-cursor-complete-guide-ja)

## Hermes

Use the sample file:

```bash
cat config/hermes.example.yaml
```

The important values are:

```yaml
base_url: https://lizh.ai/v1
api_key: ${LIZH_API_KEY}
model: kimi-k3
```

Detailed guide: [Kimi K3 in OpenClaw or Hermes](https://shop.lizh.ai/blogs/kimi-k3-api/kimi-k3-openclaw-hermes-complete-guide-vi)

## OpenClaw

Use the sample file:

```bash
cat config/openclaw.example.yaml
```

## Cost Checks

Before testing long-context tasks:

- Start with a short prompt.
- Set a small output limit.
- Review logs and cost in lizh.ai after the request.
- Compare input tokens, output tokens, and cache-hit tokens separately.

Detailed pricing guide: [Kimi K3 API pricing](https://shop.lizh.ai/blogs/kimi-k3-api/kimi-k3-pricing-complete-guide-ru)

## Useful Guides

- [Dev.to article: Kimi K3 OpenAI-compatible API](https://dev.to/_47686745be4094e3787a/how-to-use-kimi-k3-with-an-openai-compatible-api-endpoint-196l)
- [Local article source](content/devto-kimi-k3-openai-compatible-api.md)
- [How to get and use Kimi K3 API](https://shop.lizh.ai/blogs/kimi-k3-api/kimi-k3-api-key-complete-guide-ru)
- [Kimi K3 pricing guide](https://shop.lizh.ai/blogs/kimi-k3-api/kimi-k3-pricing-complete-guide-ru)
- [Kimi K3 with Cursor](https://shop.lizh.ai/blogs/kimi-k3-api/kimi-k3-cursor-complete-guide-ja)
- [Kimi K3 with Python](https://shop.lizh.ai/blogs/kimi-k3-api/kimi-k3-python-complete-guide-fr)
- [Kimi K3 with OpenClaw or Hermes](https://shop.lizh.ai/blogs/kimi-k3-api/kimi-k3-openclaw-hermes-complete-guide-vi)

## Publish The Dev.to Article

Create a Dev.to API key, then publish the Markdown article as an unpublished draft:

```bash
export DEVTO_API_KEY="your_devto_api_key"
python3 scripts/publish_devto.py content/devto-kimi-k3-openai-compatible-api.md
```

To publish publicly after review:

```bash
python3 scripts/publish_devto.py content/devto-kimi-k3-openai-compatible-api.md --publish
```

## Official Reference

For official Kimi model behavior and provider-specific features, read the Kimi documentation:

- [Kimi K3 Quickstart](https://platform.kimi.com/docs/guide/kimi-k3-quickstart)

## License

MIT
