---
title: What is async in Python?
description: Learn what async means in Python and how it enables concurrent execution without blocking your program's flow.
date: 2025-10-07
updated: 2025-10-07
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: python async, asynchronous programming, async keyword, python concurrency, async basics, Subhajit Bhar
  - name: Publisher
    content: Subhajit Bhar
  - name: author
    content: Subhajit Bhar
---

# What is async in Python?

<!-- more -->

!!! info "In short"
    `async` is a keyword in Python that marks a function as asynchronous, meaning it can pause its execution to let other tasks run while waiting for I/O operations (like API calls or file reads) to complete. Think of it like a chef who starts boiling water, then preps vegetables while waiting—instead of standing idle. It doesn't make code faster by itself, but it lets your program do multiple things "at the same time" without blocking.

## Example

Here's how you define and use an async function:

```python
import asyncio

async def fetch_data():
    print("Starting fetch...")
    await asyncio.sleep(2)  # Simulates waiting for an API
    print("Fetch complete!")
    return "Data retrieved"

# Run the async function
result = asyncio.run(fetch_data())
print(result)
```

**Output:**
```
Starting fetch...
Fetch complete!
Data retrieved
```

The `async` keyword tells Python "this function can pause and resume." The `await` inside tells it "pause here while this operation completes, but let other tasks run."

## Gotchas

- **You can't just call `fetch_data()` directly**—you need `asyncio.run()` or another event loop. Calling it without await returns a coroutine object, not the result.
- **`async` doesn't magically parallelize CPU-heavy work**. It's designed for I/O-bound tasks (network, disk) where you're mostly waiting. For CPU-intensive tasks, use multiprocessing instead.
- **Mixing sync and async code is tricky**. If you call a blocking function inside an async function without proper handling, you'll block the entire event loop.

## See also

- [What does async do in Python?](what-does-async-do-in-python.md)
- [What is asyncio in Python?](what-is-asyncio-in-python.md)
- [Python asyncio documentation](https://docs.python.org/3/library/asyncio.html)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "What is async in Python?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "async is a keyword in Python that marks a function as asynchronous, allowing it to pause execution to let other tasks run while waiting for I/O operations to complete. It enables concurrent execution without blocking the program's flow."
    }
  }]
}
</script>

