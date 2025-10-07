---
title: "How to cancel async tasks in Python?"
description: "Learn how to gracefully cancel running async tasks and handle cancellation in asyncio programs."
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: Subhajit Bhar, freelance data scientist, OCR, NLP, LLM, RAG, knowledge base, python, async, task cancellation, asyncio
  - name: Publisher
    content: Subhajit Bhar
date: 2025-10-07
updated: "2025-10-07"
---

# How to cancel async tasks in Python?

<!-- more -->

!!! info "In short"
    Call `.cancel()` on a task object to request cancellation. The task will raise `asyncio.CancelledError` at its next `await` point, which you can catch to clean up resources. Cancellation is cooperative—tasks don't stop immediately, they stop when they next yield control. Create tasks with `asyncio.create_task()` to get a task object you can cancel. Use try/except `CancelledError` to handle cleanup gracefully. Common use case: timeouts, user-initiated stops, or shutting down a server. The pattern: create tasks explicitly, save references, cancel when needed, and always handle CancelledError for cleanup.

Here's how to cancel tasks properly:

```python
import asyncio

async def long_running_task(name):
    try:
        print(f"{name}: Starting")
        for i in range(10):
            await asyncio.sleep(1)
            print(f"{name}: Step {i}")
    except asyncio.CancelledError:
        print(f"{name}: Cancelled! Cleaning up...")
        # Do cleanup here
        raise  # Re-raise to let asyncio know we handled it

async def main():
    # Create tasks (not just coroutines)
    task1 = asyncio.create_task(long_running_task("Task1"))
    task2 = asyncio.create_task(long_running_task("Task2"))
    
    # Let them run for a bit
    await asyncio.sleep(2.5)
    
    # Cancel one task
    task1.cancel()
    
    # Wait for both (task1 will raise CancelledError)
    results = await asyncio.gather(task1, task2, return_exceptions=True)
    
    for i, result in enumerate(results, 1):
        if isinstance(result, asyncio.CancelledError):
            print(f"Task{i} was cancelled")
        else:
            print(f"Task{i} result: {result}")

asyncio.run(main())
```

**Output:**
```
Task1: Starting
Task2: Starting
Task1: Step 0
Task2: Step 0
Task1: Step 1
Task2: Step 1
Task1: Cancelled! Cleaning up...
Task1 was cancelled
Task2: Step 2
...
```

Task1 stops at the next await after cancel(), runs cleanup, then raises CancelledError. Task2 continues normally.

Here's a practical pattern for timeouts:

```python
async def with_timeout():
    try:
        await asyncio.wait_for(long_running_task("TimedTask"), timeout=3)
    except asyncio.TimeoutError:
        print("Task timed out!")
```

`wait_for()` automatically cancels the task if it exceeds the timeout.

## Gotchas

* **Cancellation isn't immediate** — tasks stop at their next `await`, not instantly. If your task is doing CPU work, it won't cancel until it hits an await.
* **Must re-raise CancelledError** — after cleanup, re-raise the exception. If you swallow it, asyncio thinks the task completed normally.
* **gather() needs return_exceptions** — without it, CancelledError propagates immediately, cancelling other tasks. Use `return_exceptions=True` to collect all results.

## See also

* [How to await multiple async tasks in Python?](how-to-await-multiple-async-tasks-in-python.md)
* [How to use asyncio in Python?](how-to-use-asyncio-in-python.md)
* External: [https://docs.python.org/3/library/asyncio-task.html#task-cancellation](https://docs.python.org/3/library/asyncio-task.html#task-cancellation)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "How to cancel async tasks in Python?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Call .cancel() on a task object created with asyncio.create_task(). The task raises asyncio.CancelledError at its next await point. Catch CancelledError to clean up resources, then re-raise it. Cancellation is cooperative—tasks stop when they yield control."
    }
  }]
}
</script>

