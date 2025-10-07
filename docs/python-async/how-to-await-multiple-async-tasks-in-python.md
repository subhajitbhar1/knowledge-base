---
title: "How to await multiple async tasks in Python?"
description: "Master techniques for running multiple async tasks concurrently using gather, create_task, and as_completed in asyncio."
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: Subhajit Bhar, freelance data scientist, OCR, NLP, LLM, RAG, knowledge base, python, async, multiple tasks, asyncio.gather
  - name: Publisher
    content: Subhajit Bhar
date: 2025-10-07
updated: "2025-10-07"
---

# How to await multiple async tasks in Python?

<!-- more -->

!!! info "In short"
    Use `asyncio.gather()` to run multiple tasks concurrently and get all results at once. Use `asyncio.as_completed()` to process results as each task finishes. Use `asyncio.create_task()` to start tasks early and await them later. All three let you run tasks concurrently—the difference is how you collect results. `gather()` waits for everything and preserves order. `as_completed()` gives you results in completion order. `create_task()` gives you fine-grained control over when tasks start and finish. Choose based on whether you need ordered results, immediate processing, or custom orchestration.

Here are all the patterns for running multiple tasks:

```python
import asyncio
import time

async def fetch_data(source, delay):
    await asyncio.sleep(delay)
    return f"Data from {source}"

# Method 1: asyncio.gather() - wait for all, ordered results
async def gather_example():
    start = time.time()
    results = await asyncio.gather(
        fetch_data("API", 2),
        fetch_data("DB", 1),
        fetch_data("Cache", 0.5)
    )
    print(f"Gather ({time.time()-start:.1f}s): {results}")
    # Output: ['Data from API', 'Data from DB', 'Data from Cache']

# Method 2: asyncio.as_completed() - process as they finish
async def as_completed_example():
    start = time.time()
    tasks = [
        fetch_data("API", 2),
        fetch_data("DB", 1),
        fetch_data("Cache", 0.5)
    ]
    
    for coro in asyncio.as_completed(tasks):
        result = await coro
        elapsed = time.time() - start
        print(f"Completed ({elapsed:.1f}s): {result}")
    # Cache finishes first, then DB, then API

# Method 3: create_task() - start early, await later
async def create_task_example():
    start = time.time()
    # Start all tasks immediately
    task1 = asyncio.create_task(fetch_data("API", 2))
    task2 = asyncio.create_task(fetch_data("DB", 1))
    task3 = asyncio.create_task(fetch_data("Cache", 0.5))
    
    # Do other work while tasks run
    await asyncio.sleep(0.3)
    print("Did some work while tasks run...")
    
    # Collect results
    result1 = await task1
    result2 = await task2
    result3 = await task3
    print(f"Results: {[result1, result2, result3]}")

# Run examples
asyncio.run(gather_example())
asyncio.run(as_completed_example())
asyncio.run(create_task_example())
```

All three methods run tasks concurrently (total time ~2s, not 3.5s). The difference is result collection.

Here's the decision guide:
- Need all results in order? → `gather()`
- Want to process results immediately? → `as_completed()`
- Need fine control or want to start tasks early? → `create_task()`

## Gotchas

* **gather() stops on first exception by default** — use `return_exceptions=True` to collect all results even if some fail.
* **Don't await in a loop without create_task()** — `for x in items: await process(x)` runs sequentially. Use `gather([process(x) for x in items])` for concurrency.
* **as_completed() yields coroutines, not results** — you must await each one: `for coro in as_completed(tasks): result = await coro`.

## See also

* [How to use asyncio in Python?](how-to-use-asyncio-in-python.md)
* [How to cancel async tasks in Python?](how-to-cancel-async-tasks-in-python.md)
* External: [https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently](https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "How to await multiple async tasks in Python?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Use asyncio.gather() to run multiple tasks concurrently and get ordered results. Use asyncio.as_completed() to process results as each finishes. Use asyncio.create_task() for fine-grained control. All run tasks concurrently—choose based on result handling needs."
    }
  }]
}
</script>

