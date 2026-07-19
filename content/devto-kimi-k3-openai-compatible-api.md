---
title: "How to use Kimi K3 with an OpenAI-compatible API endpoint"
published: false
description: "A practical guide for calling Kimi K3 from Python, Node.js, cURL, Cursor, Hermes, and OpenClaw through an OpenAI-compatible API gateway."
tags: ai, api, python, opensource
canonical_url: https://github.com/Fankouzu/kimi-k3-openai-compatible-examples
---

Kimi K3 is attracting attention from developers who want a strong Chinese LLM for coding, long-context work, agents, document processing, and general API workflows.

One practical question comes up quickly:

> Can I use Kimi K3 through the same OpenAI-compatible API format that my existing tools already support?

Yes. This guide shows one working path using `lizh.ai` as an independent OpenAI-compatible API gateway.

Important note: `lizh.ai` is not the official Moonshot AI or Kimi website. It is an independent API gateway that lets you call models through a familiar `/v1/chat/completions` interface. For official model behavior and provider-specific details, always check the Kimi documentation as well.

## What you will configure

You only need three values:

```text
Base URL: https://lizh.ai/v1
Model ID: kimi-k3
API Key: your lizh.ai API key
```

You can create an API key at:

[https://lizh.ai/keys](https://lizh.ai/keys)

You can check the current model list and pricing at:

[https://lizh.ai/pricing](https://lizh.ai/pricing)

## 1. Set your API key

On macOS or Linux:

```bash
export LIZH_API_KEY="your_lizh_api_key"
```

For production usage, store this in your server secret manager, CI/CD secret store, or environment variable system. Do not hard-code it in source code.

## 2. Test Kimi K3 with cURL

Start with a small request:

```bash
curl https://lizh.ai/v1/chat/completions \
  -H "Authorization: Bearer ${LIZH_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "kimi-k3",
    "messages": [
      {
        "role": "user",
        "content": "Write a short test plan for evaluating a long-context coding model."
      }
    ],
    "max_tokens": 500
  }'
```

This is useful because it removes SDK configuration from the debugging path. If cURL works, your key, model name, and endpoint are basically correct.

## 3. Use Kimi K3 from Python

Install the OpenAI SDK:

```bash
pip install openai
```

Then call the OpenAI-compatible endpoint:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["LIZH_API_KEY"],
    base_url="https://lizh.ai/v1",
)

response = client.chat.completions.create(
    model="kimi-k3",
    messages=[
        {
            "role": "system",
            "content": "You are a concise technical assistant.",
        },
        {
            "role": "user",
            "content": "Explain when Kimi K3 is useful for long-context coding tasks.",
        },
    ],
    max_tokens=500,
)

print(response.choices[0].message.content)
```

Common checks:

- If you see an authentication error, check that `LIZH_API_KEY` is set in the same shell where you run Python.
- If you see a model error, confirm the model name on the pricing/model page.
- If the response is too long or too expensive for a test, lower `max_tokens`.

## 4. Use Kimi K3 from Node.js

Install the SDK:

```bash
npm install openai
```

Create a test script:

```js
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.LIZH_API_KEY,
  baseURL: "https://lizh.ai/v1",
});

const response = await client.chat.completions.create({
  model: "kimi-k3",
  messages: [
    {
      role: "system",
      content: "You are a concise technical assistant.",
    },
    {
      role: "user",
      content: "Give a short checklist for testing an OpenAI-compatible model gateway.",
    },
  ],
  max_tokens: 500,
});

console.log(response.choices[0].message.content);
```

This works well for quick backend tests, small agent prototypes, and API compatibility checks.

## 5. Configure Cursor

If your tool supports custom OpenAI-compatible providers, use:

```text
Provider: OpenAI-compatible
Base URL: https://lizh.ai/v1
API Key: your lizh.ai API key
Model: kimi-k3
```

Then run a small prompt first, for example:

```text
Read this file and explain the main logic in 5 bullets.
```

After the first successful request, try a real coding workflow:

- explain a large file,
- refactor a small function,
- generate tests,
- compare two implementations,
- summarize an error log.

## 6. Configure Hermes or OpenClaw

For tools that accept YAML-style provider settings, the important values are usually:

```yaml
base_url: https://lizh.ai/v1
api_key: ${LIZH_API_KEY}
model: kimi-k3
```

If the tool has a separate provider type, choose an OpenAI-compatible provider rather than an official OpenAI-only provider.

## 7. Cost and safety checklist

Before using long-context prompts:

- Start with a short prompt.
- Set a small `max_tokens` value.
- Check the current price before large tests.
- Review your usage logs after the first request.
- Keep input, output, and cache-hit costs separate when estimating cost.

This matters because long-context coding and document prompts can become large quickly.

## Complete working examples

I put the working cURL, Python, Node.js, Hermes, and OpenClaw examples in this GitHub repo:

[https://github.com/Fankouzu/kimi-k3-openai-compatible-examples](https://github.com/Fankouzu/kimi-k3-openai-compatible-examples)

Related practical guides:

- [How to get and use a Kimi K3 API key](https://shop.lizh.ai/blogs/kimi-k3-api/kimi-k3-api-key-complete-guide-ru)
- [Kimi K3 API pricing guide](https://shop.lizh.ai/blogs/kimi-k3-api/kimi-k3-pricing-complete-guide-ru)
- [Kimi K3 with Cursor](https://shop.lizh.ai/blogs/kimi-k3-api/kimi-k3-cursor-complete-guide-ja)
- [Kimi K3 with Python](https://shop.lizh.ai/blogs/kimi-k3-api/kimi-k3-python-complete-guide-fr)
- [Kimi K3 with OpenClaw or Hermes](https://shop.lizh.ai/blogs/kimi-k3-api/kimi-k3-openclaw-hermes-complete-guide-vi)

## Final thought

The fastest way to evaluate a new model is not to rebuild your whole stack. Start with one OpenAI-compatible request, verify the model name and pricing, then move the same configuration into your coding tool or agent framework.

For Kimi K3 through lizh.ai, the core configuration is:

```text
Base URL: https://lizh.ai/v1
Model ID: kimi-k3
API Key: created at https://lizh.ai/keys
```
