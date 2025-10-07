---
title: "Are lists or dictionaries faster in Python?"
description: "Compare performance of lists vs dictionaries: when each excels for lookups, insertions, and different operation types."
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: Subhajit Bhar, freelance data scientist, OCR, NLP, LLM, RAG, knowledge base, python, lists, performance
  - name: Publisher
    content: Subhajit Bhar
date: 2025-10-07
updated: "2025-10-07"
---

# Are lists or dictionaries faster in Python?

<!-- more -->

!!! info "In short"
    It depends on what kind of speed you care about. Dictionaries win when you look up items by key—they use hashing, so it's almost instant. Lists are quick when you already know *where* the item is (by index). But for searching through a list to find something? That's where dicts shine. Memory-wise, dicts cost more because of hash table overhead. The pattern: use dicts when you search by key or ID, use lists when you process items in order or by position.

In the following example, we check how long each takes to find a value in 10,000 items:

```python
import time

# Dictionary lookup (fast)
data_dict = {i: i**2 for i in range(10000)}
start = time.time()
result = 9999 in data_dict
dict_time = time.time() - start

# List lookup (slow)
data_list = list(range(10000))
start = time.time()
result = 9999 in data_list
list_time = time.time() - start

print(f"Dict lookup: {dict_time:.6f}s")
print(f"List lookup: {list_time:.6f}s")
print(f"Dict is ~{list_time/dict_time:.0f}x faster")
```

In the above code, the dictionary finishes much faster—typically around 150x. That's because checking `9999 in data_dict` jumps straight to the hash key, while the list has to check each element one by one until it finds the match.

## Gotchas

* **Comparing them blindly isn't useful** — they solve different problems. It's like asking "is a knife faster than a spoon?" Use each for what it's designed for.
* **Memory trade-off** — dicts use more RAM for that speed. For small datasets (<100 items), the difference is negligible and readability should win.
* **Dict order is now reliable** — Python 3.7+ maintains insertion order in dicts, making them viable for some list-like use cases. But lists are still clearer when order is the main point.

## See also

* [[Which is better — list or dictionary in Python?]](./which-is-better-list-or-dictionary.md)
* [[When to use list vs tuple vs dictionary vs set in Python?]](./list-vs-tuple-vs-dictionary-vs-set.md)
* External: [https://wiki.python.org/moin/TimeComplexity](https://wiki.python.org/moin/TimeComplexity)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "Are lists or dictionaries faster in Python?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "It depends on what kind of speed you care about. Dictionaries win when you look up items by key—they use hashing, so it's almost instant. Lists are quick when you already know where the item is (by index). But for searching through a list to find something? That's where dicts shine. Memory-wise, dicts cost more because of hash table overhead. The pattern: use dicts when you search by key or ID, use lists when you process items in order or by position."
    }
  }]
}
</script>
