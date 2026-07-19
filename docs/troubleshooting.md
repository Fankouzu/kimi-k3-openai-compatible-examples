# Troubleshooting

Use this checklist when a Kimi K3 request through lizh.ai fails.

## Authentication error

Check that the API key is set in the same shell where you run your command:

```bash
echo "$LIZH_API_KEY"
```

If it is empty, create or copy a key from [https://lizh.ai/keys](https://lizh.ai/keys).

## Model error

Confirm the model name:

```text
kimi-k3
```

Check current model availability at [https://lizh.ai/pricing](https://lizh.ai/pricing).

## Endpoint error

Confirm the base URL:

```text
https://lizh.ai/v1
```

The chat completions endpoint is:

```text
https://lizh.ai/v1/chat/completions
```

## Tool configuration error

If Cursor, Hermes, OpenClaw, or another tool fails:

- choose an OpenAI-compatible provider,
- set the custom base URL to `https://lizh.ai/v1`,
- use your lizh.ai API key,
- set the model to `kimi-k3`,
- test with a short prompt first.

## Official model reference

For official Kimi model behavior and provider-specific features, read the Kimi documentation:

[https://platform.kimi.com/docs/guide/kimi-k3-quickstart](https://platform.kimi.com/docs/guide/kimi-k3-quickstart)
