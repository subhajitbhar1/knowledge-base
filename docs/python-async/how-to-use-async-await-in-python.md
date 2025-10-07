---
title: "How to use async await in Python?"
description: "Master the async await syntax with practical examples and learn when and how to apply these keywords effectively."
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: Subhajit Bhar, freelance data scientist, OCR, NLP, LLM, RAG, knowledge base, python, async await, tutorial, syntax
  - name: Publisher
    content: Subhajit Bhar
date: 2025-10-07
updated: "2025-10-07"
---

# How to use async await in Python?

<!-- more -->

!!! info "In short"
    Use `async def` to define a coroutine function, and `await` inside it to pause on other async operations. The pattern: `async def my_function():` creates the function, `await other_async()` pauses until `other_async()` completes. You can only use `await` inside `async def` functions—it's a syntax error elsewhere. To run async code from normal Python, use `asyncio.run(my_function())`. Think of `async` as the declaration ("this can pause") and `await` as the action ("pause here"). They work together—you rarely use one without the other.

Here's a step-by-step guide to using async/await:

```python
import asyncio

# Step 1: Define async functions with 'async def'
async def fetch_user(user_id):
    print(f"Fetching user {user_id}...")
    await asyncio.sleep(1)  # Step 2: Use 'await' for async operations
    return {"id": user_id, "name": f"User{user_id}"}

async def fetch_posts(user_id):
    print(f"Fetching posts for user {user_id}...")
    await asyncio.sleep(0.5)
    return [f"Post1", f"Post2"]

# Step 3: Compose async functions
async def get_user_data(user_id):
    user = await fetch_user(user_id)  # Wait for user
    posts = await fetch_posts(user_id)  # Then wait for posts
    return {"user": user, "posts": posts}

# Step 4: Run from synchronous code
result = asyncio.run(get_user_data(123))
print(result)
```

**Output:**
```
Fetching user 123...
Fetching posts for user 123...
{'user': {'id': 123, 'name': 'User123'}, 'posts': ['Post1', 'Post2']}
```

Each `await` pauses the current function until the awaited operation completes. The event loop can run other tasks during these pauses.

Here's the key pattern: chain async functions with `await`, and run the top-level one with `asyncio.run()`. Don't try to call async functions like regular functions—you'll get a coroutine object, not the result.

## Gotchas

* **Forgetting await returns a coroutine** — `result = fetch_user(1)` gives you a coroutine object, not the data. Always `await` async calls.
* **Can't await in regular functions** — using `await` outside `async def` is a SyntaxError. Convert the function to async or use `asyncio.run()`.
* **Sequential awaits are sequential** — `await a(); await b()` runs them one after another. Use `asyncio.gather(a(), b())` for concurrency.

## See also

* [What is async and await in Python?](what-is-async-and-await-in-python.md)
* [How to call an async function in Python?](how-to-call-an-async-function-in-python.md)
* External: [https://docs.python.org/3/library/asyncio-task.html](https://docs.python.org/3/library/asyncio-task.html)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "How to use async await in Python?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Use async def to define coroutine functions and await inside them to pause on async operations. Chain async functions with await, and run the top-level function with asyncio.run(). Only use await inside async functions."
    }
  }]
}
</script>

