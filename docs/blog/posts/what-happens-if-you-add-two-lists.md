---
title: "What happens if you add two lists in Python?"
description: "Understand list concatenation with the + operator: how it combines lists, performance implications, and alternatives."
tags:
  - python
  - lists
  - concatenation
date: 2025-10-07
updated: "2025-10-07"
---

# What happens if you add two lists in Python?

<!-- more -->

!!! info "In short"
    Adding lists with `+` glues them together into a brand new list: `[1, 2] + [3, 4]` becomes `[1, 2, 3, 4]`. The originals don't change. Under the hood, Python creates a fresh list and copies everything over, which takes time and memory. If you're modifying a list anyway, `list1.extend(list2)` or `list1 += list2` is faster—it adds items to the first list without making a copy. Use `+` when you need both originals intact, use `extend()` when you're okay changing one in-place.

Let me show you the difference:

```python
# Concatenation creates new list
list1 = [1, 2, 3]
list2 = [4, 5]
result = list1 + list2
print(f"Result: {result}")
print(f"List1 unchanged: {list1}")

# In-place concatenation
list3 = [10, 20]
list3 += [30, 40]
print(f"List3 modified: {list3}")

# Multiple concatenations
combined = [1] + [2] + [3] + [4]
print(combined)
```

In the code above, `list1 + list2` creates a new list `[1, 2, 3, 4, 5]` while leaving both originals untouched. But `list3 += [30, 40]` modifies `list3` directly, giving us `[10, 20, 30, 40]`. The final example chains additions to produce `[1, 2, 3, 4]`.

That `+=` looks similar to `+` but behaves differently—it modifies the left side instead of creating a new list.

## Gotchas

* **Creates a new list** — `result = list1 + list2` allocates fresh memory. For huge lists, this can be expensive. If you don't need the originals, use `extend()` to save the allocation.
* **Can't mix types** — `[1, 2] + (3, 4)` crashes with TypeError. Lists only concatenate with other lists. Convert the tuple first: `[1, 2] + list((3, 4))`.
* **Chaining is inefficient** — `a + b + c + d` creates three temporary lists. For better performance, use `[*a, *b, *c, *d]` (unpacking) or `list(itertools.chain(a, b, c, d))` if you're doing this a lot.

## See also

* [[How do I add items to a Python list?]](./how-to-add-items-to-list.md)
* [[What does append() mean in Python?]](./what-does-append-mean-in-python.md)
* External: [https://docs.python.org/3/library/stdtypes.html#common-sequence-operations](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "What happens if you add two lists in Python?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Adding lists with + glues them together into a brand new list: [1, 2] + [3, 4] becomes [1, 2, 3, 4]. The originals don't change. Under the hood, Python creates a fresh list and copies everything over, which takes time and memory. If you're modifying a list anyway, list1.extend(list2) or list1 += list2 is faster—it adds items to the first list without making a copy. Use + when you need both originals intact, use extend() when you're okay changing one in-place."
    }
  }]
}
</script>
