---
title: "How to call an async function in Python?"
description: "Learn the different ways to call and execute async functions from both sync and async contexts."
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: Subhajit Bhar, freelance data scientist, OCR, NLP, LLM, RAG, knowledge base, python, async, function calls, asyncio.run
  - name: Publisher
    content: Subhajit Bhar
date: 2025-10-07
updated: "2025-10-07"
---

# How to call an async function in Python?

<!-- more -->

!!! info "In short"
    From sync code, use `asyncio.run(my_async_function())`. From async code, use `await my_async_function()`. That's it. You can't just call `my_async_function()` and get the result—it returns a coroutine object that needs to be awaited or run. Think of async functions like tasks you schedule, not functions you execute directly. `asyncio.run()` sets up the event loop and runs the coroutine, while `await` schedules it in the current loop. Choose based on your context: starting from scratch? Use `asyncio.run()`. Already in an async function? Use `await`.

Here are all the ways to call async functions:

```python
import asyncio

async def greet(name):
    await asyncio.sleep(0.1)
    return f"Hello, {name}!"

# Method 1: From sync code (entry point)
result = asyncio.run(greet("Alice"))
print(result)  # "Hello, Alice!"

# Method 2: Inside another async function
async def main():
    result = await greet("Bob")  # Use await
    print(result)

asyncio.run(main())

# Method 3: Create task for concurrent execution
async def concurrent():
    task1 = asyncio.create_task(greet("Charlie"))
    task2 = asyncio.create_task(greet("Diana"))
    
    # Wait for both
    results = await asyncio.gather(task1, task2)
    print(results)  # ['Hello, Charlie!', 'Hello, Diana!']

asyncio.run(concurrent())
```

**Wrong way:**
```python
coro = greet("Eve")  # Returns coroutine, doesn't run
print(coro)  # <coroutine object greet at 0x...>
# Python warns: RuntimeWarning: coroutine 'greet' was never awaited
```

The coroutine object is like a recipe—it describes what to do, but doesn't do it. You need `await` or `asyncio.run()` to actually execute it.

Here's what catches people: calling an async function looks normal, but it doesn't run immediately. Always await or run it.

## Gotchas

* **Don't call asyncio.run() in async code** — you'll get "RuntimeError: asyncio.run() cannot be called from a running event loop." Use `await` instead.
* **Coroutines expire** — if you create a coroutine and don't await it quickly, Python will warn you. Always await or run coroutines promptly.
* **asyncio.create_task() needs a running loop** — you can only call it inside an async function. For the entry point, use `asyncio.run()`.

## See also

* [How to use async await in Python?](how-to-use-async-await-in-python.md)
* [What is async function in Python?](what-is-async-function-in-python.md)
* External: [https://docs.python.org/3/library/asyncio-task.html](https://docs.python.org/3/library/asyncio-task.html)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "How to call an async function in Python?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "From sync code, use asyncio.run(my_async_function()). From async code, use await my_async_function(). You can't call async functions directly like regular functions—they return coroutine objects that must be awaited or run."
    }
  }]
}
</script>

