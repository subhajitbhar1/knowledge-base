---
title: "Does tuple keep order in Python?"
description: "Yes. Tuples always maintain the order you created them in. They're ordered, indexed sequences."
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: Subhajit Bhar, freelance data scientist, OCR, NLP, LLM, RAG, knowledge base, python, tuple, properties
  - name: Publisher
    content: Subhajit Bhar
date: 2025-10-07
updated: "2025-10-07"
---

# Does tuple keep order in Python?

<!-- more -->

!!! info "In short"
    Yes, absolutely. Tuples are ordered sequences—they remember exactly the sequence you created them in. `(3, 1, 2)` stays `(3, 1, 2)` forever. You can access elements by position (`my_tuple[0]`), slice them (`my_tuple[1:3]`), and iterate in predictable order. This is a defining feature of tuples, just like lists. Sets are the unordered collection—they don't guarantee sequence. If order matters (and it usually does), tuples and lists both maintain it. Tuples just freeze that order permanently.

Tuples are fully ordered collections.

They maintain the exact insertion order and support positional access.

In the following example, we demonstrate tuple ordering:

```python
# Order is preserved
my_tuple = (5, 2, 8, 1, 9)
print(my_tuple)  # (5, 2, 8, 1, 9) - exactly as created

# Access by position
print(f"First: {my_tuple[0]}")   # 5
print(f"Second: {my_tuple[1]}")  # 2
print(f"Last: {my_tuple[-1]}")   # 9

# Slicing respects order
print(my_tuple[1:4])  # (2, 8, 1)

# Iteration goes in order
for i, value in enumerate(my_tuple):
    print(f"Position {i}: {value}")

# Compare with set (unordered)
my_set = {5, 2, 8, 1, 9}
print(f"\nSet: {my_set}")  # Order may vary
# Can't do my_set[0] - no indexing in sets

# Tuples with same elements in different order are NOT equal
tuple1 = (1, 2, 3)
tuple2 = (3, 2, 1)
print(f"\n{tuple1} == {tuple2}: {tuple1 == tuple2}")  # False
```

The tuple keeps `(5, 2, 8, 1, 9)` in that exact order. Indexing works. Slicing works. Order is guaranteed.

The set may display elements in any order (though modern Python often preserves insertion order in practice).

## Gotchas

* **Immutability doesn't mean unordered** — tuples are both immutable AND ordered. Don't confuse the two properties.
* **Sorting creates new tuple** — you can't do `my_tuple.sort()` (no method). Use `sorted(my_tuple)` which returns a list, then `tuple(sorted(my_tuple))` for a sorted tuple.
* **Order equality matters** — `(1, 2)` and `(2, 1)` are different tuples. Order is part of the identity.

## See also

* [Are tuples immutable?](are-tuples-immutable.md)
* [Is Python list ordered or unordered?](is-python-list-ordered-or-unordered.md)
* External: [https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "Does tuple keep order in Python?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Yes, absolutely. Tuples are ordered sequences—they remember exactly the sequence you created them in. You can access elements by position, slice them, and iterate in predictable order. This is a defining feature of tuples, just like lists. Tuples freeze that order permanently."
    }
  }]
}
</script>
