# Python

Use the OpenAI Python SDK with the lizh.ai OpenAI-compatible endpoint.

## Install

```bash
pip install openai
```

## Set the API key

```bash
export LIZH_API_KEY="your_lizh_api_key"
```

Create a key at [https://lizh.ai/keys](https://lizh.ai/keys).

## Example

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

The same example is available in [`examples/python_chat.py`](../examples/python_chat.py).

## Cost check

Before sending long files or large prompts, check the current price at [https://lizh.ai/pricing](https://lizh.ai/pricing) and start with a small `max_tokens` value.
