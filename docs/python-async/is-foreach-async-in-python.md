---
title: "Is foreach async in Python?"
description: "Learn how to iterate asynchronously in Python and understand the difference between regular and async loops."
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: Subhajit Bhar, freelance data scientist, OCR, NLP, LLM, RAG, knowledge base, python, async, foreach, loops, iteration
  - name: Publisher
    content: Subhajit Bhar
date: 2025-10-07
updated: "2025-10-07"
---

# Is foreach async in Python?

<!-- more -->

!!! info "In short"
    Python doesn't have a built-in "foreach" keyword—it uses `for` loops. Regular `for` loops are synchronous and can't await. For async iteration, use `async for` with async iterators or generators. It looks like `async for item in async_generator():` and lets you await during each iteration. If you want to process items concurrently (like JS `Promise.all`), use `asyncio.gather()` or `asyncio.as_completed()` with list comprehension. Bottom line: regular `for` is sync, `async for` is async iteration, and `gather()` is concurrent processing. Choose based on whether you need sequential async or concurrent execution.

Here's how async iteration works in Python:

```python
import asyncio

# Regular for loop (synchronous)
def sync_example():
    for i in range(3):
        print(f"Sync: {i}")
    # Can't use await inside

# async for with async generator
async def async_generator():
    for i in range(3):
        await asyncio.sleep(0.5)
        yield i

async def async_for_example():
    async for item in async_generator():
        print(f"Async for: {item}")
        # Can await here

# Concurrent processing (like Promise.all)
async def concurrent_example():
    async def process(i):
        await asyncio.sleep(0.5)
        return f"Processed {i}"
    
    # All run concurrently
    results = await asyncio.gather(*[process(i) for i in range(3)])
    for result in results:
        print(result)

asyncio.run(async_for_example())  # Sequential async
asyncio.run(concurrent_example())  # Concurrent
```

`async for` processes items one at a time (but asynchronously). `asyncio.gather()` processes them all at once. Choose based on whether order and sequential processing matter.

Here's what JS developers often look for: `items.forEach(async item => await process(item))` doesn't work in JS (common mistake), and Python avoids this trap. Use `gather()` for concurrent foreach.

## Gotchas

* **async for needs an async iterable** — you can't use it with regular lists. Wrap in an async generator or use `asyncio.gather()` with a list comprehension.
* **Order isn't guaranteed with gather()** — results come back in completion order by default. Use `asyncio.gather()` (not `as_completed()`) to preserve order.
* **Can't await in regular for** — trying `for x in items: await foo()` is valid syntax, but the for loop itself doesn't cooperate with the event loop.

## See also

* [How to iterate over a list in Python?](../python-lists/how-to-iterate-over-a-list.md)
* [How to await multiple async tasks in Python?](how-to-await-multiple-async-tasks-in-python.md)
* External: [https://peps.python.org/pep-0492/#asynchronous-iterators-and-async-for](https://peps.python.org/pep-0492/#asynchronous-iterators-and-async-for)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "Is foreach async in Python?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Python doesn't have foreach—it uses for loops. Regular for is synchronous. For async iteration, use async for with async iterators. For concurrent processing, use asyncio.gather() with list comprehension. Choose async for for sequential async or gather() for concurrent execution."
    }
  }]
}
</script>

