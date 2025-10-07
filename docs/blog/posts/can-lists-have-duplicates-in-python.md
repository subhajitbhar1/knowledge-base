---
title: "Can lists have duplicates in Python?"
description: "Yes, Python lists allow duplicate values. Learn when duplicates are useful and how to remove them when needed."
tags:
  - python
  - lists
  - properties
date: 2025-10-07
updated: "2025-10-07"
---

# Can lists have duplicates in Python?

<!-- more -->

!!! info "In short"
    Absolutely, yes. Lists happily accept duplicates—if you add the same item three times, you'll have it three times. That's by design. Unlike sets (which automatically kick out duplicates), lists preserve every single item you add, in order. So `[1, 1, 2]` and `[1, 2]` are completely different lists. This matters when you're collecting data from loops or tracking repeated events. If you later decide you want only unique items, you can convert to a set or use a comprehension to filter.

In the following example, we create a list with duplicates and then show two ways to remove them:

```python
# Lists allow duplicates
numbers = [1, 2, 2, 3, 3, 3, 4]
print(numbers)
print(len(numbers))

# Remove duplicates (loses order)
unique = list(set(numbers))
print(unique)

# Remove duplicates (keeps order)
seen = []
[seen.append(x) for x in numbers if x not in seen]
print(seen)
```

In the code above, the original list has 7 items including duplicates. Converting to a set removes them instantly, giving us `[1, 2, 3, 4]`, though the order might shuffle. The comprehension approach preserves the original sequence while removing duplicates.

The gotcha? That `set()` trick is fast but might shuffle your order. If order matters, you need the slightly clunkier comprehension approach.

## Gotchas

* **Converting to set loses order** — well, it *used* to always lose order. In Python 3.7+, sets actually maintain insertion order, but don't rely on it for critical logic. Use it when you don't care about sequence.
* **Deduplicating is O(n²) the naive way** — that `if x not in seen` check scans the whole list each time. For thousands of items, use a set for tracking: `seen_set = set()` then check against that.
* **You can't dedupe nested lists** — `set([1, [2, 3]])` crashes because lists aren't hashable. For complex data, you'll need custom logic or convert inner lists to tuples first.

## See also

* [[What is a Python list?]](./what-is-a-python-list.md)
* [[When to use list vs tuple vs dictionary vs set in Python?]](./list-vs-tuple-vs-dictionary-vs-set.md)
* External: [https://docs.python.org/3/tutorial/datastructures.html#sets](https://docs.python.org/3/tutorial/datastructures.html#sets)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "Can lists have duplicates in Python?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Absolutely, yes. Lists happily accept duplicates—if you add the same item three times, you'll have it three times. That's by design. Unlike sets (which automatically kick out duplicates), lists preserve every single item you add, in order. So [1, 1, 2] and [1, 2] are completely different lists. This matters when you're collecting data from loops or tracking repeated events. If you later decide you want only unique items, you can convert to a set or use a comprehension to filter."
    }
  }]
}
</script>
