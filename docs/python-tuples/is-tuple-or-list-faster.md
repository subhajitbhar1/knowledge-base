---
title: "Is tuple or list faster?"
description: "Tuples are faster to create and iterate. Lists are faster for operations like append. Choose by use case, not speed."
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: Subhajit Bhar, freelance data scientist, OCR, NLP, LLM, RAG, knowledge base, python, tuple, performance
  - name: Publisher
    content: Subhajit Bhar
date: 2025-10-07
updated: "2025-10-07"
---

# Is tuple or list faster?

<!-- more -->

!!! info "In short"
    Tuples are faster to create (~2-3x) and slightly faster to iterate over. Lists are faster for append/remove operations. But honestly? The difference is negligible for most use cases (<1000 elements). Tuples win on creation because Python can optimize immutable objects better—constant folding, reuse, less memory allocation. Lists need extra space for growth. Choose tuples for semantics (immutability) and hashability, not micro-optimization. If you're creating millions of small sequences in a tight loop, tuples are measurably faster. Otherwise, pick what makes your code clearer.

Tuples are generally faster, but the reasons matter more than the raw speed.

The performance advantage comes from immutability.

In the following example, we compare creation and iteration speed:

```python
import timeit

# Creation speed
tuple_time = timeit.timeit("(1, 2, 3, 4, 5)", number=1000000)
list_time = timeit.timeit("[1, 2, 3, 4, 5]", number=1000000)

print(f"Tuple creation: {tuple_time:.4f}s")
print(f"List creation: {list_time:.4f}s")
print(f"Tuples are {list_time/tuple_time:.2f}x faster\n")

# Iteration speed (minimal difference)
tuple_iter = timeit.timeit(
    "for x in (1, 2, 3, 4, 5): pass", 
    number=1000000
)
list_iter = timeit.timeit(
    "for x in [1, 2, 3, 4, 5]: pass",
    number=1000000
)

print(f"Tuple iteration: {tuple_iter:.4f}s")
print(f"List iteration: {list_iter:.4f}s")

# But lists are faster for modifications
import sys
t = (1, 2, 3, 4, 5)
l = [1, 2, 3, 4, 5]

print(f"\nTuple size: {sys.getsizeof(t)} bytes")
print(f"List size: {sys.getsizeof(l)} bytes")
```

Tuples create faster (often 2-3x) because Python doesn't need to over-allocate space for growth. Iteration is comparable. Lists use more memory because they reserve space for future appends.

But if you're appending constantly, lists win—tuples need to create entirely new tuples each time.

## Gotchas

* **Small differences** — for everyday code with <100 elements, you won't notice the speed difference. Don't choose based on this alone.
* **Context matters** — creating tuples in a hot loop (millions of times)? Measurable win. Occasional use? Irrelevant.
* **Lists have methods** — the speed of `list.append()` vs tuple concatenation `t + (new_item,)` is huge. Lists win for dynamic operations.

## See also

* [What are the advantages of a tuple over a list?](advantages-of-tuple-over-list.md)
* [Is a tuple faster than an array?](is-tuple-faster-than-array.md)
* External: [https://wiki.python.org/moin/TimeComplexity](https://wiki.python.org/moin/TimeComplexity)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "Is tuple or list faster?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Tuples are faster to create (~2-3x) and slightly faster to iterate over. Lists are faster for append/remove operations. The difference is negligible for most use cases. Choose tuples for semantics (immutability) and hashability, not micro-optimization."
    }
  }]
}
</script>
