---
title: "How to debug async Python code?"
description: "Learn effective techniques and tools for debugging asynchronous Python programs and troubleshooting common async issues."
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: Subhajit Bhar, freelance data scientist, OCR, NLP, LLM, RAG, knowledge base, python, async, debugging, asyncio
  - name: Publisher
    content: Subhajit Bhar
date: 2025-10-07
updated: "2025-10-07"
---

# How to debug async Python code?

<!-- more -->

!!! info "In short"
    Enable asyncio's debug mode with `asyncio.run(main(), debug=True)` or set `PYTHONASYNCIODEBUG=1` to catch common mistakes like unawaited coroutines or slow callbacks. Use `print()` strategically (or logging) to trace execution flow—async makes stack traces confusing. For interactive debugging, `pdb` works but loses context when switching tasks. Better options: `aioconsole` for async REPL, or IDEs like PyCharm/VS Code with async-aware breakpoints. The key insight: async debugging is harder because execution jumps between tasks, so focus on logging task states and using debug mode warnings.

Here are practical debugging techniques:

```python
import asyncio
import logging

# Enable detailed logging
logging.basicConfig(level=logging.DEBUG)

async def problematic_task(task_id):
    print(f"Task {task_id}: Starting")
    try:
        await asyncio.sleep(1)
        if task_id == 2:
            raise ValueError("Task 2 failed!")
        print(f"Task {task_id}: Completed")
    except Exception as e:
        print(f"Task {task_id}: Error - {e}")
        raise

async def main():
    # Gather with return_exceptions to see all errors
    results = await asyncio.gather(
        problematic_task(1),
        problematic_task(2),
        problematic_task(3),
        return_exceptions=True  # Don't stop on first error
    )
    
    for i, result in enumerate(results, 1):
        if isinstance(result, Exception):
            print(f"Task {i} failed: {result}")

# Run with debug mode
asyncio.run(main(), debug=True)
```

Debug mode will warn you about:
- Coroutines that were never awaited
- Tasks that take >100ms (configurable)
- Exceptions not retrieved from tasks

Here's a lifesaver: use `asyncio.create_task()` with `name` parameter for easier tracking: `task = asyncio.create_task(fetch(), name="fetch_user")`. Then errors show the task name.

## Gotchas

* **Stack traces are confusing** — they show event loop internals, not just your code. Look for your function names buried in the trace.
* **print() might interleave** — multiple tasks can print simultaneously. Use logging with task IDs for clarity.
* **Deadlocks are silent** — if all tasks are waiting on each other, your program just hangs. Use `asyncio.wait_for(coro, timeout=5)` to add timeouts.

## See also

* [How async works in Python?](how-async-works-in-python.md)
* [How to cancel async tasks in Python?](how-to-cancel-async-tasks-in-python.md)
* External: [https://docs.python.org/3/library/asyncio-dev.html](https://docs.python.org/3/library/asyncio-dev.html)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "How to debug async Python code?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Enable asyncio debug mode with asyncio.run(main(), debug=True) to catch unawaited coroutines and slow callbacks. Use logging with task IDs to trace execution, and asyncio.gather with return_exceptions=True to see all errors. Consider async-aware debuggers like PyCharm."
    }
  }]
}
</script>

