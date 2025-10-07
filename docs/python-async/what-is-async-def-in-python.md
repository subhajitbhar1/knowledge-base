---
title: What is async def in Python?
description: Understand the async def syntax for defining asynchronous functions in Python and how it differs from regular def.
date: 2025-10-07
updated: 2025-10-07
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: python async def, async syntax, coroutine definition, asynchronous functions, python async, Subhajit Bhar
  - name: Publisher
    content: Subhajit Bhar
  - name: author
    content: Subhajit Bhar
---

# What is async def in Python?

<!-- more -->

!!! info "In short"
    `async def` is the syntax for defining an asynchronous function (coroutine) in Python. It's just like `def`, but with `async` in front. When you use `async def`, Python knows this function can pause with `await` and play nice with other async code. The function signature looks the same—parameters, type hints, docstrings all work normally—but the behavior changes: calling it returns a coroutine object instead of executing immediately. It's the literal declaration that makes a function asynchronous.

## Example

Here's how `async def` looks in practice:

```python
import asyncio

# Regular function
def regular_greet(name):
    return f"Hello, {name}!"

# Async function - just add 'async' before 'def'
async def async_greet(name):
    await asyncio.sleep(0.5)  # Can use await inside
    return f"Hello, {name}!"

# Usage
print(regular_greet("Alice"))  # Hello, Alice!

# Async version needs await or asyncio.run()
result = asyncio.run(async_greet("Bob"))
print(result)  # Hello, Bob!
```

**Output:**
```
Hello, Alice!
Hello, Bob!
```

The only syntactic difference is the `async` keyword, but it fundamentally changes how the function works—it becomes a coroutine that must be awaited.

## Gotchas

- **You can't have a regular function and async function with the same name**—Python treats them differently, but it's confusing and leads to mistakes.
- **async def without any await is legal but pointless**. Python won't warn you, but you're adding async overhead with no benefit.
- **Type hints work normally**: `async def fetch(url: str) -> dict:` is perfectly valid and recommended.

## See also

- [What is async function in Python?](what-is-async-function-in-python.md)
- [How to create async functions in Python?](how-to-create-async-functions-in-python.md)
- [PEP 492 - Coroutines with async and await syntax](https://www.python.org/dev/peps/pep-0492/)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "What is async def in Python?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "async def is the syntax for defining an asynchronous function (coroutine) in Python. It's like regular def but with async in front, telling Python the function can pause with await and must be awaited when called."
    }
  }]
}
</script>

