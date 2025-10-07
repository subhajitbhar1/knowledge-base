---
title: "What are the disadvantages of list in Python?"
description: "Lists are slower for lookups, use more memory, can't be dict keys, and their mutability can cause bugs."
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: Subhajit Bhar, freelance data scientist, OCR, NLP, LLM, RAG, knowledge base, python, tuple, comparison
  - name: Publisher
    content: Subhajit Bhar
date: 2025-10-07
updated: "2025-10-07"
---

# What are the disadvantages of list in Python?

<!-- more -->

!!! info "In short"
    Lists are slower for membership tests (`x in list` is O(n)), use more memory than tuples due to over-allocation for growth, and can't be dict keys or set members because they're not hashable. Their mutability is both strength and weakness—it enables bugs when lists get modified unexpectedly, especially when passed to functions or used as default arguments. For large datasets, lists are slower than NumPy arrays for numeric ops. And inserting/deleting from the middle is slow (O(n)). Choose sets for lookups, tuples for immutability, deques for queues, or NumPy for math.

Lists trade versatility for optimization—they're general-purpose, not specialized.

Here are the key limitations:

In the following example, we demonstrate list performance issues:

```python
import sys

# Memory overhead
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
print(f"List: {sys.getsizeof(my_list)} bytes")
print(f"Tuple: {sys.getsizeof(my_tuple)} bytes")

# Slow membership testing
large_list = list(range(10000))
# This checks every element until found
result = 9999 in large_list  # Slow!

# Compare with set
large_set = set(range(10000))
result = 9999 in large_set  # Fast! O(1)

# Can't be dict key
coords = [10, 20]
try:
    cache = {coords: "value"}
except TypeError as e:
    print(f"Dict key error: {e}")

# Mutability gotcha
def add_item(items=[]):  # DANGER!
    items.append("new")
    return items

print(add_item())  # ['new']
print(add_item())  # ['new', 'new'] - Oops!
```

The list uses 88 bytes vs tuple's 64. The membership test walks through thousands of items. And that default argument bug is infamous—the empty list is created once and reused.

These aren't bugs in lists—they're trade-offs for flexibility.

## Gotchas

* **Membership testing** — if you're doing `if x in my_list` repeatedly, convert to a set. That O(n) adds up fast.
* **Mutable defaults** — never use `def func(items=[])`. Use `def func(items=None): if items is None: items = []`.
* **Shared references** — `list2 = list1` doesn't copy. Both names point to the same list. Use `list2 = list1.copy()` for independence.

## See also

* [What are the advantages of a tuple over a list?](advantages-of-tuple-over-list.md)
* [What is the difference between a tuple and a list?](difference-between-tuple-and-list.md)
* External: [https://wiki.python.org/moin/TimeComplexity](https://wiki.python.org/moin/TimeComplexity)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "What are the disadvantages of list in Python?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Lists are slower for membership tests (x in list is O(n)), use more memory than tuples, and can't be dict keys or set members because they're not hashable. Their mutability enables bugs when lists get modified unexpectedly. For large datasets, lists are slower than NumPy arrays for numeric operations."
    }
  }]
}
</script>
