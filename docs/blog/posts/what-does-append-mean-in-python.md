---
title: "What does append() mean in Python?"
description: "Understand the append() method: how it adds items to lists, its performance characteristics, and common mistakes to avoid."
tags:
  - python
  - lists
  - methods
date: 2025-10-07
updated: "2025-10-07"
---

# What does append() mean in Python?

<!-- more -->

!!! info "In short"
    `.append()` sticks one item onto the end of your list. That's it. It modifies the list in-place and doesn't return anything (well, it returns `None`, but you ignore that). Need to build a list in a loop? Append is your friend—it's fast, averaging O(1) time. The catch: it takes exactly one thing. Pass it a list and that whole list becomes a single nested element. Most beginners do that once, see the weird result, and never make the mistake again. For multiple items, you want `.extend()` instead.

Let me show you how append works:

```python
# Basic append
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)

# Append in a loop
squares = []
for i in range(5):
    squares.append(i**2)
print(squares)

# Appending a list creates nesting
items = [1, 2]
items.append([3, 4])
print(items)  # Note: [3, 4] is one element
```

In the example above, the first append gives us `[1, 2, 3, 4]`. The loop builds up `[0, 1, 4, 9, 16]` one square at a time. But that last one? It creates `[1, 2, [3, 4]]`—the list `[3, 4]` became a single nested item, not two separate numbers.

See that last one? `[3, 4]` became a single nested item, not two separate numbers.

## Gotchas

* **Returns None** — writing `result = my_list.append(5)` makes `result` equal to `None`. Append modifies the list and returns nothing useful. This trips up folks coming from JavaScript or other languages.
* **Only one argument** — `my_list.append(1, 2)` throws an error. If you've got multiple things, either append them one by one in a loop or use `.extend([1, 2])`.
* **In-place modification** — pass a list to a function that appends to it? The original list changes. Sometimes that's what you want, sometimes it's a nasty surprise. Make a copy first if you need the original intact.

## See also

* [[How do I add items to a Python list?]](./how-to-add-items-to-list.md)
* [[How do I remove elements from a Python list?]](./how-to-remove-elements-from-list.md)
* External: [https://docs.python.org/3/tutorial/datastructures.html#more-on-lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "What does append() mean in Python?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": ".append() sticks one item onto the end of your list. That's it. It modifies the list in-place and doesn't return anything (well, it returns None, but you ignore that). Need to build a list in a loop? Append is your friend—it's fast, averaging O(1) time. The catch: it takes exactly one thing. Pass it a list and that whole list becomes a single nested element. Most beginners do that once, see the weird result, and never make the mistake again. For multiple items, you want .extend() instead."
    }
  }]
}
</script>
