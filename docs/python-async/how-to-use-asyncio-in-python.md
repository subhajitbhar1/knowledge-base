---
title: "How to use asyncio in Python?"
description: "Learn practical patterns for using asyncio to write concurrent Python programs with async/await syntax."
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: Subhajit Bhar, freelance data scientist, OCR, NLP, LLM, RAG, knowledge base, python, asyncio, async await, tutorial
  - name: Publisher
    content: Subhajit Bhar
date: 2025-10-07
updated: "2025-10-07"
---

# How to use asyncio in Python?

<!-- more -->

!!! info "In short"
    Start with `asyncio.run()` to execute your main async function. Define functions with `async def`, use `await` for I/O operations, and `asyncio.gather()` to run multiple tasks concurrently. The pattern is: create async functions, await them where needed, and let `asyncio.run()` handle the event loop. For real I/O, replace blocking libraries (like `requests`) with async alternatives (like `aiohttp`). The learning curve is steep at first, but the core pattern—define with `async def`, pause with `await`—becomes second nature quickly.

Here's a complete example showing common asyncio patterns:

```python
import asyncio

async def fetch_data(source, delay):
    print(f"Fetching from {source}...")
    await asyncio.sleep(delay)  # Simulates I/O
    return f"Data from {source}"

async def main():
    # Run tasks concurrently
    results = await asyncio.gather(
        fetch_data("API", 2),
        fetch_data("Database", 1),
        fetch_data("Cache", 0.5)
    )
    
    for result in results:
        print(result)

# Entry point - runs the event loop
asyncio.run(main())
```

**Output:**
```
Fetching from API...
Fetching from Database...
Fetching from Cache...
Data from API
Data from Database
Data from Cache
```

All three `fetch_data` calls start immediately, run concurrently, and finish in ~2 seconds (not 3.5). `asyncio.gather()` waits for all of them and returns results in order.

Here's what often confuses people: you need async-compatible libraries. Using `time.sleep()` or `requests.get()` will block the entire event loop—use `asyncio.sleep()` and `aiohttp` instead.

## Gotchas

* **Don't call asyncio.run() twice** — it creates a new event loop. Call it once at your program's entry point, not inside async functions.
* **Use async libraries** — regular I/O libraries will block. Look for async alternatives: `aiohttp` for HTTP, `aiofiles` for file I/O, `asyncpg` for PostgreSQL.
* **Exception handling matters** — if one task in `gather()` raises an exception, it cancels the others by default. Use `return_exceptions=True` to collect errors instead.

## See also

* [What is asyncio in Python?](what-is-asyncio-in-python.md)
* [How to use async await in Python?](how-to-use-async-await-in-python.md)
* External: [https://docs.python.org/3/library/asyncio-task.html](https://docs.python.org/3/library/asyncio-task.html)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "How to use asyncio in Python?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Use asyncio by defining functions with async def, awaiting I/O operations, and running your main async function with asyncio.run(). Use asyncio.gather() to run multiple tasks concurrently, and replace blocking libraries with async alternatives."
    }
  }]
}
</script>

