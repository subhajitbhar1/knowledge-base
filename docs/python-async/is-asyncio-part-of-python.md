---
title: Is asyncio part of Python?
description: Learn whether asyncio is built into Python or requires separate installation, and which Python versions include it.
date: 2025-10-07
updated: 2025-10-07
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: python asyncio, standard library, python modules, asyncio version, python async, Subhajit Bhar
  - name: Publisher
    content: Subhajit Bhar
  - name: author
    content: Subhajit Bhar
---

# Is asyncio part of Python?

<!-- more -->

!!! info "In short"
    Yes, `asyncio` is part of Python's standard library—it's been included since Python 3.4 (released in 2014). You don't need to install anything extra; just `import asyncio` and you're ready to go. The API has improved significantly over the years (Python 3.7 added `asyncio.run()`, 3.11 made it faster), but the core has been stable and built-in for a decade now. It's as "standard" as `json` or `datetime`.

## Example

You can verify it's built-in by importing without installation:

```python
import asyncio
import sys

print(f"Python version: {sys.version}")
print(f"asyncio location: {asyncio.__file__}")
print(f"asyncio version: {asyncio.__version__ if hasattr(asyncio, '__version__') else 'N/A'}")

# It just works - no pip install needed
async def hello():
    await asyncio.sleep(0.1)
    return "asyncio is built-in!"

result = asyncio.run(hello())
print(result)
```

**Output:**
```
Python version: 3.11.x
asyncio location: /usr/lib/python3.11/asyncio/__init__.py
asyncio version: N/A
asyncio is built-in!
```

The path shows it's in Python's standard library directory, not in site-packages where third-party libraries live.

## Gotchas

- **Python 3.4-3.6 have older asyncio APIs**. Code using `asyncio.run()` won't work in Python 3.6 or earlier—you'll need to use `loop.run_until_complete()` instead.
- **Third-party async libraries exist** (like Trio, Curio), but they're not replacements for asyncio—they're alternatives with different design philosophies.
- **asyncio doesn't include HTTP clients**. For that, you need third-party libraries like `aiohttp` or `httpx`.

## See also

- [What is asyncio in Python?](what-is-asyncio-in-python.md)
- [How to use asyncio in Python?](how-to-use-asyncio-in-python.md)
- [Python asyncio documentation](https://docs.python.org/3/library/asyncio.html)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "Is asyncio part of Python?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Yes, asyncio is part of Python's standard library since Python 3.4. No separate installation is needed—just import asyncio and start using it for asynchronous programming."
    }
  }]
}
</script>

