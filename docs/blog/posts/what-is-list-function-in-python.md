---
title: "What is list() in Python?"
description: "Understand the list() constructor function: how it converts iterables to lists and when to use it versus literal syntax."
tags:
  - python
  - lists
  - functions
date: 2025-10-07
updated: "2025-10-07"
---

# What is list() in Python?

<!-- more -->

!!! info "In short"
    `list()` is a built-in function that converts things into lists. Call it with no arguments and you get an empty list. Give it something iterable—a string, tuple, range, whatever—and it unpacks all the items into a fresh list. Use `list()` when converting other data types or when you need explicit type conversion. For creating lists from scratch with known values, literal syntax `[1, 2, 3]` is clearer and slightly faster than `list((1, 2, 3))`. Think of `list()` as the "turn this into a list" function, not your go-to creation tool.

Here are some practical examples of using `list()`:

```python
# Empty list
empty = list()

# Convert string to list of characters
chars = list("Python")

# Convert tuple to list
numbers = list((1, 2, 3, 4))

# Convert range to list
sequence = list(range(5))

print(chars)
print(numbers)
print(sequence)
```

In the code above, `list("Python")` splits the string into individual characters: `['P', 'y', 't', 'h', 'o', 'n']`. The tuple `(1, 2, 3, 4)` becomes a list with the same values. And `range(5)` expands into `[0, 1, 2, 3, 4]`.

One neat trick: `list(existing_list)` creates a shallow copy. Handy when you need independence from the original.

## Gotchas

* **Brackets are more idiomatic** — writing `list()` for an empty list works, but `[]` is what most Python code uses. Save `list()` for when you're actually converting something.
* **Shallow copy behavior** — `list(old_list)` copies the list structure but not nested objects. If `old_list` contains other lists, those inner lists are still shared.
* **Can't pass numbers** — `list(5)` crashes with TypeError. You probably wanted `list(range(5))` to get `[0, 1, 2, 3, 4]`. Easy mistake.

## See also

* [[How do you create a list in Python?]](./how-to-create-list-in-python.md)
* [[How do I declare a list in Python?]](./how-to-declare-list-in-python.md)
* External: [https://docs.python.org/3/library/functions.html#func-list](https://docs.python.org/3/library/functions.html#func-list)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "What is list() in Python?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "list() is a built-in function that converts things into lists. Call it with no arguments and you get an empty list. Give it something iterable—a string, tuple, range, whatever—and it unpacks all the items into a fresh list. Use list() when converting other data types or when you need explicit type conversion. For creating lists from scratch with known values, literal syntax [1, 2, 3] is clearer and slightly faster than list((1, 2, 3)). Think of list() as the turn this into a list function, not your go-to creation tool."
    }
  }]
}
</script>
