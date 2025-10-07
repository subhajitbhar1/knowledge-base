---
title: "What is a decorator in Python (in async context)?"
description: "Learn how decorators work with async functions and discover common async decorator patterns in Python."
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: Subhajit Bhar, freelance data scientist, OCR, NLP, LLM, RAG, knowledge base, python, decorators, async, functions
  - name: Publisher
    content: Subhajit Bhar
date: 2025-10-07
updated: "2025-10-07"
---

# What is a decorator in Python (in async context)?

<!-- more -->

!!! info "In short"
    Decorators are functions that wrap other functions to add behavior—like logging, timing, or caching. With async functions, decorators work the same way, but they must preserve the async nature. An async decorator typically wraps an async function with another async function using `@wraps` from `functools`. Common async decorators: retry logic, rate limiting, timing, caching. The key rule: if decorating an async function, the wrapper should also be async (use `async def`). If decorating sync functions, use regular decorators. They're powerful for cross-cutting concerns without cluttering your core logic.

Here's how to create async decorators:

```python
import asyncio
import functools
import time

# Async decorator for timing
def async_timer(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        start = time.time()
        result = await func(*args, **kwargs)
        duration = time.time() - start
        print(f"{func.__name__} took {duration:.2f}s")
        return result
    return wrapper

# Async decorator for retries
def async_retry(max_attempts=3):
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"Attempt {attempt + 1} failed: {e}")
                    await asyncio.sleep(1)
        return wrapper
    return decorator

# Usage
@async_timer
@async_retry(max_attempts=3)
async def fetch_data():
    await asyncio.sleep(1)
    return "Data"

asyncio.run(fetch_data())
```

**Output:**
```
fetch_data took 1.00s
```

The decorators add timing and retry logic without modifying `fetch_data()`. Stack them to combine behaviors.

Here's a common mistake: forgetting `async def` in the wrapper when decorating async functions. The decorator will work but won't be awaitable, breaking your async chain.

## Gotchas

* **Must use async def for async decorators** — if your wrapper isn't async, you can't await the decorated function properly.
* **Order matters** — decorators stack from bottom to top. `@timer @retry` applies retry first, then timing.
* **functools.wraps is essential** — without it, your decorated function loses its name, docstring, and other metadata. Always use it.

## See also

* [How to create async functions in Python?](how-to-create-async-functions-in-python.md)
* [What is async function in Python?](what-is-async-function-in-python.md)
* External: [https://realpython.com/primer-on-python-decorators/](https://realpython.com/primer-on-python-decorators/)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "What is a decorator in Python (in async context)?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Decorators are functions that wrap other functions to add behavior like logging or timing. With async functions, decorators must preserve the async nature by using async def in the wrapper. Common async decorators include retry logic, rate limiting, and caching."
    }
  }]
}
</script>

