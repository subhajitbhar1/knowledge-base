---
title: What is asyncio in Python?
description: Understand asyncio, Python's built-in library for writing asynchronous programs using async/await syntax and event loops.
date: 2025-10-07
updated: 2025-10-07
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: python asyncio, asyncio library, event loop, asynchronous programming, async await, Subhajit Bhar
  - name: Publisher
    content: Subhajit Bhar
  - name: author
    content: Subhajit Bhar
---

# What is asyncio in Python?

<!-- more -->

!!! info "In short"
    `asyncio` is Python's standard library for writing asynchronous code. It provides an event loop that manages async functions, letting you run multiple I/O-bound tasks concurrently without threads or multiprocessing. Think of it as a traffic controller for your async functions—it decides when each task runs, pauses, and resumes. It's been part of the standard library since Python 3.4 and is the go-to tool for async web servers, API clients, and anything that spends time waiting.

## Example

Here's a simple asyncio program that runs two tasks concurrently:

```python
import asyncio

async def task_one():
    print("Task 1: Starting")
    await asyncio.sleep(2)
    print("Task 1: Done")

async def task_two():
    print("Task 2: Starting")
    await asyncio.sleep(1)
    print("Task 2: Done")

async def main():
    await asyncio.gather(task_one(), task_two())

asyncio.run(main())
```

**Output:**
```
Task 1: Starting
Task 2: Starting
Task 2: Done
Task 1: Done
```

Both tasks start immediately, but Task 2 finishes first because it sleeps for less time. The event loop switches between them while they're waiting.

## Gotchas

- **asyncio.run() creates a new event loop each time**. Don't call it inside another async function—you'll get a "RuntimeError: asyncio.run() cannot be called from a running event loop."
- **Not all libraries are async-compatible**. Using `requests` or `time.sleep()` in async code will block the event loop. Use `aiohttp` and `asyncio.sleep()` instead.
- **Debugging async code is harder** because stack traces show the event loop machinery, not just your code. Tools like `asyncio.run(debug=True)` help.

## See also

- [How to use asyncio in Python?](how-to-use-asyncio-in-python.md)
- [Is asyncio part of Python?](is-asyncio-part-of-python.md)
- [Python asyncio documentation](https://docs.python.org/3/library/asyncio.html)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "What is asyncio in Python?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "asyncio is Python's standard library for writing asynchronous code. It provides an event loop that manages async functions, allowing you to run multiple I/O-bound tasks concurrently without threads or multiprocessing."
    }
  }]
}
</script>

