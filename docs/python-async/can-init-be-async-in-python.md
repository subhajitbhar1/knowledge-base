---
title: "Can __init__ be async in Python?"
description: "Understand why __init__ can't be async and learn the proper patterns for asynchronous object initialization."
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: Subhajit Bhar, freelance data scientist, OCR, NLP, LLM, RAG, knowledge base, python, async, init, class initialization
  - name: Publisher
    content: Subhajit Bhar
date: 2025-10-07
updated: "2025-10-07"
---

# Can __init__ be async in Python?

<!-- more -->

!!! info "In short"
    No, `__init__` cannot be async. Python's object instantiation expects `__init__` to return `None` immediately, not a coroutine. Making `__init__` async would break the fundamental `obj = MyClass()` syntax. Instead, use a factory pattern: define an async class method that creates the instance, then calls an async setup method. Or use `__await__` with `__new__` for advanced cases. The common pattern is `obj = await MyClass.create()`. It's a design limitation, not a bug—synchronous initialization keeps Python's object model simple.

Here's the right way to handle async initialization:

```python
import asyncio

class Database:
    def __init__(self):
        self.connection = None
    
    async def connect(self):
        """Async setup after __init__"""
        print("Connecting...")
        await asyncio.sleep(1)  # Simulates async I/O
        self.connection = "connected"
        return self
    
    @classmethod
    async def create(cls):
        """Factory method for async creation"""
        self = cls()
        await self.connect()
        return self

# Usage
async def main():
    db = await Database.create()
    print(f"DB status: {db.connection}")

asyncio.run(main())
```

The `create()` class method constructs the object, then awaits the async setup. This pattern is clean and widely used in async codebases.

Here's what often trips people up: trying `async def __init__` gives a `TypeError: __init__() should return None, not 'coroutine'`. Python enforces synchronous construction to keep the language consistent.

## Gotchas

* **You can't await MyClass()** — constructors are synchronous. Use a factory method or context manager instead.
* **`__await__` exists but is tricky** — you can define `__await__` to make an object awaitable, but it's advanced and rarely needed. Stick with factory methods.
* **Context managers work great** — use `async with await MyClass.create():` for resources that need async setup and cleanup.

## See also

* [How to create async functions in Python?](how-to-create-async-functions-in-python.md)
* [What is async function in Python?](what-is-async-function-in-python.md)
* External: [https://docs.python.org/3/reference/datamodel.html#object.__await__](https://docs.python.org/3/reference/datamodel.html#object.__await__)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "Can __init__ be async in Python?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "No, __init__ cannot be async because Python expects it to return None immediately, not a coroutine. Use an async factory method pattern instead: create a classmethod that constructs the object and calls an async setup method."
    }
  }]
}
</script>

