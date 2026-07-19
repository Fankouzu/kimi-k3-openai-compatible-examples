# OpenClaw

OpenClaw can use Kimi K3 when configured with an OpenAI-compatible API gateway.

## Values

```yaml
base_url: https://lizh.ai/v1
api_key: ${LIZH_API_KEY}
model: kimi-k3
```

The sample file is available at [`config/openclaw.example.yaml`](../config/openclaw.example.yaml).

## Setup

1. Create an API key at [https://lizh.ai/keys](https://lizh.ai/keys).
2. Set `LIZH_API_KEY`.
3. Configure OpenClaw with `https://lizh.ai/v1`.
4. Use `kimi-k3` as the model.
5. Run a short coding prompt first.

## First prompt

```text
Summarize this repository and suggest the first three files I should read.
```
