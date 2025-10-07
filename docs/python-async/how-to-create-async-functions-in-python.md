---
title: "How to create async functions in Python?"
description: "Step-by-step guide to defining and structuring asynchronous functions using async def in Python."
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: Subhajit Bhar, freelance data scientist, OCR, NLP, LLM, RAG, knowledge base, python, async functions, async def, tutorial
  - name: Publisher
    content: Subhajit Bhar
date: 2025-10-07
updated: "2025-10-07"
---

# How to create async functions in Python?

<!-- more -->

!!! info "In short"
    Creating async functions is simple: replace `def` with `async def`. That's the syntax. Inside, use `await` to pause on other async operations. The function becomes a coroutine—calling it returns a coroutine object that must be awaited. Structure your async functions like regular functions: parameters, docstrings, return values, type hints all work normally. The only difference: you can use `await` inside, and callers must await the result. Start with your I/O operations (API calls, database queries, file reads), make those async, then make the functions calling them async, and so on up the chain.

Here's the anatomy of async functions:

```python
import asyncio
from typing import List, Dict

# Basic async function
async def simple_async():
    await asyncio.sleep(1)
    return "Done"

# Async function with parameters and type hints
async def fetch_user(user_id: int) -> Dict[str, any]:
    """
    Fetches user data from a database.
    
    Args:
        user_id: The user's ID
        
    Returns:
        Dictionary with user data
    """
    print(f"Fetching user {user_id}...")
    await asyncio.sleep(0.5)  # Simulates DB query
    return {"id": user_id, "name": f"User{user_id}"}

# Async function calling other async functions
async def get_users_batch(user_ids: List[int]) -> List[Dict]:
    """Fetches multiple users concurrently"""
    tasks = [fetch_user(uid) for uid in user_ids]
    users = await asyncio.gather(*tasks)
    return users

# Async function with error handling
async def safe_fetch(user_id: int) -> Dict[str, any]:
    try:
        return await fetch_user(user_id)
    except Exception as e:
        print(f"Error fetching user {user_id}: {e}")
        return {"id": user_id, "error": str(e)}

# Run it
async def main():
    user = await fetch_user(123)
    print(user)
    
    users = await get_users_batch([1, 2, 3])
    print(users)

asyncio.run(main())
```

Every function that needs to await something must be async. It's contagious by design—async spreads up the call chain.

Here's the pattern: identify I/O points (network, disk, sleep), make those functions async with `async def` and `await`, then make their callers async, until you reach your entry point where you use `asyncio.run()`.

## Gotchas

* **Forgetting async def makes await illegal** — using `await` in a regular function is a SyntaxError. The function signature must be `async def`.
* **Async without await is wasteful** — if your async function never uses `await`, it's pointless overhead. Just use a regular function.
* **Return types are normal** — don't return coroutines or awaitable objects unless you mean to. Return regular values—asyncio handles the wrapping.

## See also

* [What is async def in Python?](what-is-async-def-in-python.md)
* [How to call an async function in Python?](how-to-call-an-async-function-in-python.md)
* External: [https://docs.python.org/3/library/asyncio-task.html](https://docs.python.org/3/library/asyncio-task.html)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "How to create async functions in Python?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Create async functions by replacing def with async def. Use await inside to pause on async operations. The function returns a coroutine that must be awaited. Parameters, type hints, docstrings, and return values work normally—only difference is you can await inside."
    }
  }]
}
</script>

