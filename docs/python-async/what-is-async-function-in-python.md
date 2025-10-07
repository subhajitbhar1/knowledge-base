---
title: What is async function in Python?
description: Learn about async functions (coroutines) in Python and how they differ from regular synchronous functions.
date: 2025-10-07
updated: 2025-10-07
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: python async function, coroutines, asynchronous functions, async def, python concurrency, Subhajit Bhar
  - name: Publisher
    content: Subhajit Bhar
  - name: author
    content: Subhajit Bhar
---

# What is async function in Python?

<!-- more -->

!!! info "In short"
    An async function is a function defined with `async def` instead of just `def`. It's technically called a coroutine function, and when you call it, you get a coroutine object that must be awaited or run by an event loop. Async functions can use `await` to pause and let other tasks run while waiting for I/O. They're the building blocks of asynchronous programming—each one represents a task that can cooperate with others instead of blocking the whole program.

## Example

Here's a comparison between regular and async functions:

```python
import asyncio
import time

def sync_function():
    print("Sync: Starting")
    time.sleep(1)
    print("Sync: Done")
    return "Sync result"

async def async_function():
    print("Async: Starting")
    await asyncio.sleep(1)
    print("Async: Done")
    return "Async result"

# Regular function - just call it
result1 = sync_function()
print(result1)

# Async function - need asyncio.run()
result2 = asyncio.run(async_function())
print(result2)
```

**Output:**
```
Sync: Starting
Sync: Done
Sync result
Async: Starting
Async: Done
Async result
```

The difference: `sync_function()` blocks everything while sleeping, but `async_function()` can let other tasks run during the sleep.

## Gotchas

- **Async functions aren't async all the way down**. If you call a blocking sync function inside an async function, you still block the event loop. Use async libraries like `aiohttp` instead of `requests`.
- **You can't await in a sync function**. Once you go async, everything that calls it needs to be async too (it's "contagious").
- **Async functions have overhead**. For simple, fast operations, they're slower than regular functions. Use them when you're actually waiting for I/O.

## See also

- [How to create async functions in Python?](how-to-create-async-functions-in-python.md)
- [How to call an async function in Python?](how-to-call-an-async-function-in-python.md)
- [Python coroutines documentation](https://docs.python.org/3/library/asyncio-task.html)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "What is async function in Python?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "An async function is a function defined with async def that returns a coroutine object when called. It can use await to pause execution and let other tasks run while waiting for I/O operations. Async functions are the building blocks of asynchronous programming in Python."
    }
  }]
}
</script>

