---
title: "Is Python single threaded?"
description: "Understand Python's threading model, the Global Interpreter Lock (GIL), and how it affects concurrent execution."
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: Subhajit Bhar, freelance data scientist, OCR, NLP, LLM, RAG, knowledge base, python, threading, GIL, concurrency
  - name: Publisher
    content: Subhajit Bhar
date: 2025-10-07
updated: "2025-10-07"
---

# Is Python single threaded?

<!-- more -->

!!! info "In short"
    Python can use multiple threads, but the Global Interpreter Lock (GIL) means only one thread executes Python bytecode at a time. So yes, Python is effectively single-threaded for CPU-bound work—multiple threads won't speed up pure computation. But threads still help for I/O-bound tasks (network, disk) because the GIL releases during I/O waits. Think of it like a single-lane bridge: many cars (threads) can queue up, but only one crosses at a time. For true parallelism, you need multiprocessing, not threading.

Here's a quick demonstration of threading behavior:

```python
import threading
import time

def cpu_bound_task(n):
    """Lots of computation"""
    count = 0
    for i in range(n):
        count += i ** 2
    return count

start = time.time()

# Sequential
cpu_bound_task(10_000_000)
cpu_bound_task(10_000_000)
print(f"Sequential: {time.time() - start:.2f}s")

# Threaded
start = time.time()
t1 = threading.Thread(target=cpu_bound_task, args=(10_000_000,))
t2 = threading.Thread(target=cpu_bound_task, args=(10_000_000,))
t1.start(); t2.start()
t1.join(); t2.join()
print(f"Threaded: {time.time() - start:.2f}s")
# Similar times due to GIL
```

Both approaches take roughly the same time because the GIL ensures only one thread runs Python code at once. Threading doesn't help with CPU-bound tasks—sometimes it's even slower due to context switching overhead.

Here's what surprises people: Python has threads, but the GIL serializes their execution. For I/O (waiting for APIs, files), threads work great. For computation (crunching numbers), use `multiprocessing` instead.

## Gotchas

* **Threads won't speed up CPU work** — due to the GIL, threading can't leverage multiple CPU cores for pure Python computation. Use `multiprocessing.Pool` for that.
* **I/O-bound is the sweet spot** — threads excel when waiting for network, disk, or user input. The GIL releases during I/O, letting other threads run.
* **Not all Python is GIL-limited** — NumPy, C extensions, and some libraries release the GIL, so threading can be effective there.

## See also

* [Can Python be multithreaded?](can-python-be-multithreaded.md)
* [Which is better threading or asyncio in Python?](which-is-better-threading-or-asyncio.md)
* External: [https://realpython.com/python-gil/](https://realpython.com/python-gil/)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "Is Python single threaded?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Python can use multiple threads, but the Global Interpreter Lock (GIL) means only one thread executes Python bytecode at a time. Python is effectively single-threaded for CPU-bound work, but threads help with I/O-bound tasks where the GIL releases during waits."
    }
  }]
}
</script>

