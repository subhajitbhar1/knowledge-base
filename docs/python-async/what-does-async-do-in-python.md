---
title: What does async do in Python?
description: Discover how the async keyword transforms regular functions into coroutines that can pause and resume execution.
date: 2025-10-07
updated: 2025-10-07
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: python async, async keyword, coroutines, asynchronous functions, python concurrency, Subhajit Bhar
  - name: Publisher
    content: Subhajit Bhar
  - name: author
    content: Subhajit Bhar
---

# What does async do in Python?

<!-- more -->

!!! info "In short"
    The `async` keyword transforms a regular function into a coroutine—a special type of function that can pause its execution with `await` and let other code run. It doesn't run the function in the background or make it parallel; instead, it makes the function cooperative, allowing it to voluntarily yield control. When you call an async function, it returns a coroutine object that needs to be awaited or run by an event loop. It's the foundation for Python's cooperative multitasking model.

## Example

Here's what happens when you use `async`:

```python
import asyncio

async def greet(name):
    print(f"Hello, {name}!")
    await asyncio.sleep(1)
    print(f"Goodbye, {name}!")
    return f"{name} greeted"

# Calling it directly returns a coroutine object
coro = greet("Alice")
print(coro)  # <coroutine object greet at 0x...>

# You need to await it or run it with asyncio.run()
result = asyncio.run(greet("Bob"))
print(result)
```

**Output:**
```
<coroutine object greet at 0x...>
Hello, Bob!
Goodbye, Bob!
Bob greeted
```

The `async` keyword makes `greet()` return a coroutine instead of executing immediately. You must await it or use `asyncio.run()` to actually run it.

## Gotchas

- **Forgetting to await gives you a coroutine object, not the result**. Python 3.7+ will warn you: "coroutine 'greet' was never awaited."
- **async alone doesn't make code concurrent**. You need to use `await asyncio.gather()` or `asyncio.create_task()` to run multiple coroutines concurrently.
- **You can't use await outside async functions**. Trying to call `await` in regular functions gives a SyntaxError.

## See also

- [What is async function in Python?](what-is-async-function-in-python.md)
- [What is async and await in Python?](what-is-async-and-await-in-python.md)
- [Python coroutines documentation](https://docs.python.org/3/library/asyncio-task.html)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "What does async do in Python?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "The async keyword transforms a regular function into a coroutine that can pause execution with await and let other code run. It makes the function cooperative, allowing it to voluntarily yield control in Python's cooperative multitasking model."
    }
  }]
}
</script>

