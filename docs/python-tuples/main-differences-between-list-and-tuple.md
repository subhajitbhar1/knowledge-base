---
title: "What are the main differences between list and tuple in Python?"
description: "Mutability: lists change, tuples don't. Syntax: [] vs (). Performance: tuples are faster. Use cases: different."
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

# What are the main differences between list and tuple in Python?

<!-- more -->

!!! info "In short"
    Four main differences: (1) **Mutability** - lists can be modified, tuples can't. (2) **Syntax** - lists use square brackets `[]`, tuples use parentheses `()`. (3) **Hashability** - tuples can be dict keys, lists can't. (4) **Performance** - tuples are slightly faster and use less memory. (5) **Methods** - lists have append/remove/etc, tuples have minimal methods. (6) **Semantics** - lists say "working collection," tuples say "fixed structure." Choose lists for collections you'll modify. Choose tuples for immutable data like coordinates, returns, or config.

The differences boil down to mutability and everything that flows from it.

Here's a side-by-side comparison:

In the following example, we compare all major differences:

```python
# 1. MUTABILITY
my_list = [1, 2, 3]
my_list.append(4)  # ✓ Works
my_list[0] = 99    # ✓ Works

my_tuple = (1, 2, 3)
# my_tuple.append(4)   # ✗ AttributeError
# my_tuple[0] = 99     # ✗ TypeError

# 2. SYNTAX
list_example = [1, 2, 3]   # Square brackets
tuple_example = (1, 2, 3)  # Parentheses

# 3. HASHABILITY
tuple_dict = {(1, 2): "value"}  # ✓ Works
try:
    list_dict = {[1, 2]: "value"}  # ✗ TypeError
except TypeError as e:
    print(f"List as key: {e}")

# 4. PERFORMANCE
import sys
print(f"List size: {sys.getsizeof([1, 2, 3])} bytes")
print(f"Tuple size: {sys.getsizeof((1, 2, 3))} bytes")

# 5. METHODS
print(f"List methods: {len([m for m in dir(list) if not m.startswith('_')])}")
print(f"Tuple methods: {len([m for m in dir(tuple) if not m.startswith('_')])}")

# 6. USE CASES
# List: dynamic collection
shopping_cart = ["apple", "banana"]
shopping_cart.append("orange")

# Tuple: fixed structure
coordinates = (40.7128, -74.0060)  # Won't change
rgb_color = (255, 0, 0)  # Red, immutable

# 7. CONVERSION (easy both ways)
converted_tuple = tuple(my_list)
converted_list = list(my_tuple)
```

Lists are flexible and mutable. Tuples are fixed and immutable. That single difference affects everything else.

Choose based on whether your data should change.

## Gotchas

* **Both are ordered** — don't confuse immutability with lack of order. Both maintain sequence.
* **Both allow duplicates** — `[1, 1, 2]` and `(1, 1, 2)` both work fine. Sets are the ones that don't allow dupes.
* **Performance difference is minor** — for <1000 elements, you won't notice the speed difference. Choose for semantics.

## See also

* [What is the difference between a tuple and a list?](difference-between-tuple-and-list.md)
* [What are the advantages of a tuple over a list?](advantages-of-tuple-over-list.md)
* External: [https://docs.python.org/3/tutorial/datastructures.html](https://docs.python.org/3/tutorial/datastructures.html)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "What are the main differences between list and tuple in Python?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Four main differences: Mutability - lists can be modified, tuples can't. Syntax - lists use [], tuples use (). Hashability - tuples can be dict keys, lists can't. Performance - tuples are slightly faster. Choose lists for collections you'll modify. Choose tuples for immutable data."
    }
  }]
}
</script>
