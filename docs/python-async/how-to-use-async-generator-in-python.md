---
title: "How to use async generator in Python?"
description: "Learn how to create and consume async generators for streaming data asynchronously in Python."
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: Subhajit Bhar, freelance data scientist, OCR, NLP, LLM, RAG, knowledge base, python, async generator, async iteration
  - name: Publisher
    content: Subhajit Bhar
date: 2025-10-07
updated: "2025-10-07"
---

# How to use async generator in Python?

<!-- more -->

!!! info "In short"
    An async generator is an async function that uses `yield` instead of `return`, letting you stream values asynchronously. Define with `async def`, yield values, and consume with `async for`. They're perfect for processing large datasets, streaming APIs, or reading files incrementally without blocking. Think of them like regular generators, but with async superpowers—each `yield` is an await point where other tasks can run. Use them when you'd use a generator in sync code but need async I/O between yields.

Here's how to create and use async generators:

```python
import asyncio

# Define an async generator
async def fetch_pages(n):
    """Streams page data one at a time"""
    for page in range(1, n + 1):
        print(f"Fetching page {page}...")
        await asyncio.sleep(0.5)  # Simulates async I/O
        yield {"page": page, "data": f"Content {page}"}

# Consume with async for
async def main():
    async for page_data in fetch_pages(3):
        print(f"Processing: {page_data}")
        # Do work with each page as it arrives

asyncio.run(main())
```

**Output:**
```
Fetching page 1...
Processing: {'page': 1, 'data': 'Content 1'}
Fetching page 2...
Processing: {'page': 2, 'data': 'Content 2'}
Fetching page 3...
Processing: {'page': 3, 'data': 'Content 3'}
```

Each iteration fetches and processes one page at a time. The generator pauses at `yield` and `await`, letting other tasks run in between.

Here's a practical use case: streaming large CSV files or paginated API results without loading everything into memory. You process items as they arrive, reducing memory usage.

## Gotchas

* **Must use async for** — regular `for` loops won't work with async generators. You'll get "TypeError: 'async_generator' object is not iterable."
* **Can't mix yield and return values** — `return some_value` in an async generator raises StopAsyncIteration, but the value is lost. Use `yield` for all outputs.
* **Error handling is tricky** — exceptions in async generators can be hard to trace. Wrap the `async for` in try/except to catch them.

## See also

* [How to use asyncio in Python?](how-to-use-asyncio-in-python.md)
* [What is async function in Python?](what-is-async-function-in-python.md)
* External: [https://peps.python.org/pep-0525/](https://peps.python.org/pep-0525/)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "How to use async generator in Python?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Create async generators with async def and yield. Consume them with async for. They let you stream values asynchronously, perfect for processing large datasets or streaming APIs without blocking. Each yield is an await point where other tasks can run."
    }
  }]
}
</script>

