---
title: "Is Python synchronous or asynchronous?"
description: "Clarify Python's execution model and understand how it supports both synchronous and asynchronous programming paradigms."
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: Subhajit Bhar, freelance data scientist, OCR, NLP, LLM, RAG, knowledge base, python, sync, async, execution model
  - name: Publisher
    content: Subhajit Bhar
date: 2025-10-07
updated: "2025-10-07"
---

# Is Python synchronous or asynchronous?

<!-- more -->

!!! info "In short"
    Python is synchronous by default, but it supports asynchronous programming when you opt in. Regular Python code executes line by line, blocking at each step until complete. When you use `async def` and `await`, you enable cooperative multitasking where tasks can voluntarily yield control during I/O waits. So the answer is: Python is fundamentally synchronous, but you can write asynchronous code when needed. It's not one or the other—it's both, depending on how you write your code.

Here's how both models work side by side:

```python
import time
import asyncio

# Synchronous execution
def task_sync(name, delay):
    print(f"{name} starting")
    time.sleep(delay)  # Blocks everything
    print(f"{name} done")

task_sync("Task 1", 2)
task_sync("Task 2", 1)
# Total time: ~3 seconds (sequential)

# Asynchronous execution
async def task_async(name, delay):
    print(f"{name} starting")
    await asyncio.sleep(delay)  # Yields control
    print(f"{name} done")

async def main():
    await asyncio.gather(
        task_async("Task A", 2),
        task_async("Task B", 1)
    )

asyncio.run(main())
# Total time: ~2 seconds (concurrent)
```

Synchronous code runs top-to-bottom with no interruptions. Asynchronous code can interleave tasks while waiting for I/O. Both are valid Python—you choose based on your needs.

Here's the key insight: Python's execution is sequential unless you explicitly make it cooperative with async/await. It's not like JavaScript, where async is deeply embedded in the language runtime.

## Gotchas

* **Synchronous is the default** — if you don't use `async`/`await`, your code is synchronous. No surprises.
* **You can't mix them carelessly** — calling synchronous blocking code in an async function blocks the entire event loop. Use `loop.run_in_executor()` or `asyncio.to_thread()` to handle sync calls.
* **Async doesn't mean parallel** — Python's GIL means async code still runs one operation at a time. It's concurrent (interleaved), not parallel (simultaneous).

## See also

* [Is Python asynchronous?](is-python-asynchronous.md)
* [How async works in Python?](how-async-works-in-python.md)
* External: [https://realpython.com/async-io-python/](https://realpython.com/async-io-python/)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "Is Python synchronous or asynchronous?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Python is synchronous by default, with code executing line by line. However, Python supports asynchronous programming through async/await syntax when you opt in. It's fundamentally synchronous but allows asynchronous code when needed."
    }
  }]
}
</script>

