# cURL

cURL is the fastest way to verify that the endpoint, API key, and model name work before debugging SDK or app configuration.

## Set the API key

```bash
export LIZH_API_KEY="your_lizh_api_key"
```

## Send a request

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

The same example is available in [`examples/curl_chat.sh`](../examples/curl_chat.sh).

## Expected result

If the request succeeds, you should receive a JSON response with a model answer. If it fails, see [Troubleshooting](troubleshooting.md).
