---
title: "How async works in Python?"
description: "Understand the mechanics behind Python's async/await, event loops, and cooperative multitasking model."
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: Subhajit Bhar, freelance data scientist, OCR, NLP, LLM, RAG, knowledge base, python, async, event loop, coroutines
  - name: Publisher
    content: Subhajit Bhar
date: 2025-10-07
updated: "2025-10-07"
---

# How async works in Python?

<!-- more -->

!!! info "In short"
    Async works through an event loop that manages coroutines. When you `await` something, your coroutine pauses and returns control to the event loop, which then runs other coroutines that are ready. Think of it like a juggler: the event loop keeps multiple balls (coroutines) in the air, giving each one attention when it's ready to move forward. When a coroutine hits `await` on I/O, it says "I'm waiting, run someone else," and the loop switches to another task. This cooperative multitasking means tasks voluntarily yield—no preemption, no threads.

Here's a visualization of how the event loop switches between tasks:

```python
import asyncio
import time

async def task(name, delay):
    print(f"[{time.time():.2f}] {name}: Started")
    await asyncio.sleep(delay)
    print(f"[{time.time():.2f}] {name}: Done")

async def main():
    await asyncio.gather(
        task("Task-A", 2),
        task("Task-B", 1),
        task("Task-C", 1.5)
    )

asyncio.run(main())
```

**Output:**
```
[12.34] Task-A: Started
[12.34] Task-B: Started
[12.34] Task-C: Started
[13.34] Task-B: Done
[13.84] Task-C: Done
[14.34] Task-A: Done
```

All tasks start immediately (they're queued), but the event loop interleaves them. Each `await` is a yield point where the loop can switch to another task. The loop keeps cycling through ready tasks until all are done.

Here's the insight that clicks for most people: async isn't magic parallelism. It's organized waiting. The event loop doesn't make things faster—it just prevents idle time from blocking everything else.

## Gotchas

* **Blocking calls freeze everything** — if you use `time.sleep()` or `requests.get()` in async code, the entire event loop stops. Always use async equivalents.
* **Await is required** — forgetting `await` on an async function call returns a coroutine object, not the result. Python warns you, but it's a common mistake.
* **Only one loop runs at a time** — you can't nest event loops easily. Use `asyncio.run()` once at the top level, not inside async functions.

## See also

* [What is async and await in Python?](what-is-async-and-await-in-python.md)
* [How to use asyncio in Python?](how-to-use-asyncio-in-python.md)
* External: [https://realpython.com/async-io-python/](https://realpython.com/async-io-python/)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "How async works in Python?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Async works through an event loop that manages coroutines. When you await, your coroutine pauses and returns control to the event loop, which runs other ready coroutines. This cooperative multitasking lets tasks voluntarily yield during I/O waits."
    }
  }]
}
</script>

