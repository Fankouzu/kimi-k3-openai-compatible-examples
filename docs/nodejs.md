# Node.js

Use the OpenAI Node.js SDK with the lizh.ai OpenAI-compatible endpoint.

## Install

```bash
npm install openai
```

## Set the API key

```bash
export LIZH_API_KEY="your_lizh_api_key"
```

## Example

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

The same example is available in [`examples/node_chat.mjs`](../examples/node_chat.mjs).
