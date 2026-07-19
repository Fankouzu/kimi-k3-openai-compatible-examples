# Hermes

Hermes can be configured with an OpenAI-compatible endpoint when the provider settings allow a custom base URL, API key, and model name.

## Values

```yaml
base_url: https://lizh.ai/v1
api_key: ${LIZH_API_KEY}
model: kimi-k3
```

The sample file is available at [`config/hermes.example.yaml`](../config/hermes.example.yaml).

## Setup

1. Create an API key at [https://lizh.ai/keys](https://lizh.ai/keys).
2. Set `LIZH_API_KEY` in your shell or secret manager.
3. Configure Hermes with `https://lizh.ai/v1` as the base URL.
4. Set the model name to `kimi-k3`.
5. Start with a short prompt before testing long-context tasks.

## Notes

If Hermes has separate provider choices, select an OpenAI-compatible or custom OpenAI provider rather than an official OpenAI-only preset.
