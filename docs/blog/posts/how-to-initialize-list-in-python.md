---
title: "How do I start or initialize a list in Python?"
description: "Quick guide to initializing Python lists: empty lists, pre-filled values, default sizes, and best practices for list setup."
tags:
  - python
  - lists
  - creation
date: 2025-10-07
updated: "2025-10-07"
---

# How do I start or initialize a list in Python?

<!-- more -->

!!! info "In short"
    Starting a list is dead simple: `my_list = []` for empty, or fill it upfront with `[0] * 5` for five zeros. Need something fancier? List comprehensions work great: `[i for i in range(10)]`. The one trap? Never use a list as a default function parameter like `def func(items=[]):`. That creates a single shared list across all calls—classic Python gotcha. Instead, use `def func(items=None):` and check inside: `if items is None: items = []`. That gives each call its own fresh list.

Here are the main ways to initialize lists:

```python
# Empty list
empty = []

# Pre-filled with same value
zeros = [0] * 5

# Sequential values
numbers = list(range(1, 6))

# Complex initialization (2D list)
matrix = [[0 for _ in range(3)] for _ in range(3)]

print(zeros)
print(numbers)
print(matrix[0])
```

In the above code, the multiplication `[0] * 5` gives us `[0, 0, 0, 0, 0]`. The range becomes `[1, 2, 3, 4, 5]`. And that nested comprehension creates a 3x3 grid, with the first row showing as `[0, 0, 0]`.

That matrix example shows proper 2D initialization. Don't use `[[0] * 3] * 3`—it creates shared rows.

## Gotchas

* **Mutable default parameters are shared** — writing `def add_item(items=[]):` means every call without arguments uses the *same* list. Add something once, it persists. Always use `None` as the default and create the list inside.
* **Multiplication with nested structures** — `[[0] * 3] * 3` looks fine but creates three references to the same inner list. Change one row, change all. Use nested comprehensions instead.
* **Don't over-allocate** — lists grow automatically. You rarely need to pre-fill with `[None] * 1000` unless you're doing something specific with indices. Start small and append as needed.

## See also

* [[How do you create a list in Python?]](./how-to-create-list-in-python.md)
* [[How do I declare a list in Python?]](./how-to-declare-list-in-python.md)
* External: [https://docs.python.org/3/tutorial/datastructures.html](https://docs.python.org/3/tutorial/datastructures.html)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "How do I start or initialize a list in Python?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Starting a list is dead simple: my_list = [] for empty, or fill it upfront with [0] * 5 for five zeros. Need something fancier? List comprehensions work great: [i for i in range(10)]. The one trap? Never use a list as a default function parameter like def func(items=[]): That creates a single shared list across all calls—classic Python gotcha. Instead, use def func(items=None): and check inside: if items is None: items = []. That gives each call its own fresh list."
    }
  }]
}
</script>
