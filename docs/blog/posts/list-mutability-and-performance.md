---
title: "How does list mutability affect performance?"
description: "Understand performance implications of mutable lists: in-place operations, memory allocation, and when immutability helps."
tags:
  - python
  - lists
  - performance
date: 2025-10-07
updated: "2025-10-07"
---

# How does list mutability affect performance?
<!-- more -->

!!! info "In short"
    Mutability enables fast in-place operations—`.append()`, `.sort()`, `.reverse()` modify directly without copying, saving time and memory. But it's a double-edged sword. When functions might modify shared lists, you end up making defensive copies (`list.copy()`), which negates the speed benefit. Lists over-allocate memory for growth, using more RAM than tuples. For read-only data, tuples are lighter and enable optimizations. The trade-off: mutability gives you efficient modifications but at the cost of higher memory use and potential hidden copies when you need safety.

## Example (runnable)

```python
import sys

# In-place modification (efficient)
<!-- more -->
numbers = [1, 2, 3, 4, 5]
numbers.reverse()  # O(n), no new list
print(numbers)

# Memory comparison
<!-- more -->
list_obj = [1, 2, 3, 4, 5]
tuple_obj = (1, 2, 3, 4, 5)
print(f"List: {sys.getsizeof(list_obj)} bytes")
print(f"Tuple: {sys.getsizeof(tuple_obj)} bytes")

# Defensive copy cost
<!-- more -->
def process(items):
    safe = items.copy()  # Extra work due to mutability
    safe.sort()
    return safe

result = process([3, 1, 2])
print(result)
```

**Expected output:**
```
[5, 4, 3, 2, 1]
List: 104 bytes
Tuple: 88 bytes
[1, 2, 3]
```

That 16-byte difference is the cost of flexibility—over-allocation for future growth.

## Gotchas

* **Hidden copies everywhere** — good defensive programming means copying mutable arguments. So you end up copying anyway, losing the modification speed benefit.
* **Over-allocation compounds** — lists pre-allocate ~12% extra space. For millions of small lists, that's real memory waste. Consider tuples or arrays for fixed data.
* **Shared state bugs** — `list2 = list1` creates a reference. Modify one, both change. This forces more copies than you'd need with immutable structures.

## See also

* [[What are the disadvantages of using lists in Python?]](./disadvantages-of-using-lists-in-python.md)
* [[What is the difference between a tuple and a list?]](./difference-between-tuple-and-list.md)
* External: [https://wiki.python.org/moin/TimeComplexity](https://wiki.python.org/moin/TimeComplexity)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "How does list mutability affect performance?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Mutability enables fast in-place operations—.append(), .sort(), .reverse() modify directly without copying, saving time and memory. But it's a double-edged sword. When functions might modify shared lists, you end up making defensive copies (list.copy()), which negates the speed benefit. Lists over-allocate memory for growth, using more RAM than tuples. For read-only data, tuples are lighter and enable optimizations. The trade-off: mutability gives you efficient modifications but at the cost of higher memory use and potential hidden copies when you need safety."
    }
  }]
}
</script>
