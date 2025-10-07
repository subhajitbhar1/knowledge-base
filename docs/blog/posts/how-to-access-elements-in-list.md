---
title: "How do you access elements in a Python list?"
description: "Master list indexing: positive and negative indices, accessing first/last elements, and avoiding index errors."
tags:
  - python
  - lists
  - indexing
date: 2025-10-07
updated: "2025-10-07"
---

# How do you access elements in a Python list?

<!-- more -->

!!! info "In short"
    Square brackets with the position: `my_list[0]` gets the first item. Python counts from zero, so `[0]` is first, `[1]` is second, and so on. Negative numbers count backwards: `[-1]` is last, `[-2]` is second-to-last. Try to access something that doesn't exist and you'll get an `IndexError`. To be safe, check the length first or use slicing (which doesn't crash on bad indices). It's simple once you remember: zero is the beginning, negatives work backwards from the end.

Here's how indexing works in practice:

```python
# Basic indexing
fruits = ["apple", "banana", "cherry", "date"]

print(fruits[0])    # First element
print(fruits[2])    # Third element
print(fruits[-1])   # Last element
print(fruits[-2])   # Second to last

# Length check before accessing
if len(fruits) > 3:
    print(fruits[3])
```

Running this code prints "apple" (first), "cherry" (third), "date" (last), and "cherry" again (second-to-last). The length check safely accesses index 3, which gives us "date".

That negative indexing is genuinely handy—no need to calculate `len(list) - 1` for the last item.

## Gotchas

* **Zero-based indexing** — this is the classic beginner stumble. The first item is `[0]`, not `[1]`. Coming from math or Excel, it feels wrong. You'll adjust.
* **IndexError is common** — accessing `list[5]` when there are only 3 items crashes hard. Always validate if you're unsure, or use try/except if you're feeling defensive.
* **Negative indices aren't magic** — `list[-100]` on a 3-item list still raises IndexError. Negatives just mean "count from the end", they don't wrap around infinitely or anything clever.

## See also

* [[What is [-1] in a Python list?]](./what-is-negative-one-in-list.md)
* [[How do you slice a list in Python?]](./how-to-slice-a-list-in-python.md)
* External: [https://docs.python.org/3/tutorial/introduction.html#lists](https://docs.python.org/3/tutorial/introduction.html#lists)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "How do you access elements in a Python list?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Square brackets with the position: my_list[0] gets the first item. Python counts from zero, so [0] is first, [1] is second, and so on. Negative numbers count backwards: [-1] is last, [-2] is second-to-last. Try to access something that doesn't exist and you'll get an IndexError. To be safe, check the length first or use slicing (which doesn't crash on bad indices). It's simple once you remember: zero is the beginning, negatives work backwards from the end."
    }
  }]
}
</script>
