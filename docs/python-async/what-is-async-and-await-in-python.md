---
title: What is async and await in Python?
description: Learn how async and await work together to enable cooperative multitasking in Python's asynchronous programming model.
date: 2025-10-07
updated: 2025-10-07
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: python async await, asynchronous programming, coroutines, cooperative multitasking, python concurrency, Subhajit Bhar
  - name: Publisher
    content: Subhajit Bhar
  - name: author
    content: Subhajit Bhar
---

# What is async and await in Python?

<!-- more -->

!!! info "In short"
    `async` and `await` are two keywords that work together to enable cooperative multitasking. `async` marks a function as asynchronous (a coroutine), and `await` is used inside that function to pause execution while waiting for another async operation to complete. Think of `async` as "this function can take breaks" and `await` as "take a break here." While one task is waiting, the event loop can run other tasks. They're Python's answer to non-blocking I/O without the complexity of threads or callbacks.

## Example

Here's how they work together:

```python
import asyncio

async def make_coffee():
    print("Grinding beans...")
    await asyncio.sleep(2)  # Pause here - let other tasks run
    print("Coffee ready!")
    return "Coffee"

async def make_toast():
    print("Toasting bread...")
    await asyncio.sleep(1)  # Another pause point
    print("Toast ready!")
    return "Toast"

async def make_breakfast():
    # Run both concurrently
    coffee, toast = await asyncio.gather(
        make_coffee(),
        make_toast()
    )
    print(f"Breakfast: {coffee} and {toast}")

asyncio.run(make_breakfast())
```

**Output:**
```
Grinding beans...
Toasting bread...
Toast ready!
Coffee ready!
Breakfast: Coffee and Toast
```

Toast finishes first even though coffee started first—that's cooperative multitasking. Each `await` is a yield point where control can switch.

## Gotchas

- **await only works inside async functions**. Using it in regular functions gives `SyntaxError: 'await' outside async function`.
- **Not everything is awaitable**. You can only await coroutines, tasks, and futures. Regular functions or objects will give a TypeError.
- **Forgetting await on an async call** means you get a coroutine object, not the result. Python will warn you: "coroutine was never awaited."

## See also

- [How to use async await in Python?](how-to-use-async-await-in-python.md)
- [Why use async await in Python?](why-use-async-await-in-python.md)
- [Python asyncio documentation](https://docs.python.org/3/library/asyncio.html)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "What is async and await in Python?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "async and await are keywords that work together for cooperative multitasking. async marks a function as asynchronous, and await pauses execution inside that function while waiting for another async operation, allowing other tasks to run."
    }
  }]
}
</script>

