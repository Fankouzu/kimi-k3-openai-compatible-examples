# Pricing and Cost Checks

Before testing long-context or agent workflows, check the current model price at:

[https://lizh.ai/pricing](https://lizh.ai/pricing)

## Basic cost habits

- Start with a short prompt.
- Set a small output limit.
- Review usage logs after the first request.
- Compare input tokens, output tokens, and cache-hit tokens separately.
- Increase prompt size only after the small request works.

## Why this matters

Coding agents and long-context prompts can send large inputs. A small cURL or SDK test tells you whether the configuration works before you spend tokens on a full workflow.

## Recommended first test

```text
Explain what this function does in 5 bullets.
```

Then move to larger tasks such as:

- repository summaries,
- file-by-file review,
- test generation,
- error-log analysis,
- refactoring plans.
