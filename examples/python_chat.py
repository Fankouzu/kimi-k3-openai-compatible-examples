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
