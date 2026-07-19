# Cursor

Cursor can use Kimi K3 when configured with an OpenAI-compatible provider.

## Values

```text
Provider: OpenAI-compatible
Base URL: https://lizh.ai/v1
API Key: your lizh.ai API key
Model: kimi-k3
```

Create an API key at [https://lizh.ai/keys](https://lizh.ai/keys).

Find current model names and prices at [https://lizh.ai/pricing](https://lizh.ai/pricing).

## First test

Use a small prompt first:

```text
Read this file and explain the main logic in 5 bullets.
```

After that works, try a real coding workflow:

- explain a large file,
- refactor a small function,
- generate tests,
- compare two implementations,
- summarize an error log.

## Tip

For large repository prompts, check cost before testing long-context requests.
