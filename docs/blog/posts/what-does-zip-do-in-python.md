---
title: "What does zip() do in Python?"
description: "Learn how zip() pairs elements from multiple iterables, creates tuples, and enables parallel iteration over lists."
tags:
  - python
  - lists
  - functions
date: 2025-10-07
updated: "2025-10-07"
---

# What does zip() do in Python?

<!-- more -->

!!! info "In short"
    `zip()` pairs up items from two or more lists (or any iterables) position by position. Give it `[1, 2, 3]` and `['a', 'b', 'c']`, and you get tuples: `(1, 'a')`, `(2, 'b')`, `(3, 'c')`. It stops when the shortest list runs out. Perfect for iterating over multiple lists in parallel or creating dictionaries from separate key and value lists. The result is an iterator, so wrap it in `list()` if you need to see or reuse the full output. Think of it as a zipper joining two sides together—hence the name.

Here's how you'd typically use zip:

```python
# Basic zipping
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
combined = list(zip(names, ages))
print(combined)

# Create dictionary
person_dict = dict(zip(names, ages))
print(person_dict)

# Parallel iteration
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
```

Running the code above produces `[('Alice', 25), ('Bob', 30), ('Charlie', 35)]` as a list of tuples. Converting to a dict gives us `{'Alice': 25, 'Bob': 30, 'Charlie': 35}`. And the loop prints each person's name with their age on separate lines.

That dict creation is elegant—two lists become a dictionary in one line.

## Gotchas

* **Stops at shortest** — `zip([1, 2, 3], ['a'])` only produces `(1, 'a')`. The extra 2 and 3 get ignored. If you need all items, use `itertools.zip_longest()` which pads with None.
* **Returns iterator in Python 3** — you can only loop through it once. If you need to use it multiple times, convert to a list first: `list(zip(...))`.
* **Unzipping trick** — `zip(*zipped)` transposes data. If `zipped = [(1, 'a'), (2, 'b')]`, then `list(zip(*zipped))` gives `[(1, 2), ('a', 'b')]`. Reads backwards but super useful.

## See also

* [[How do you iterate over a list in Python?]](./how-to-iterate-over-a-list.md)
* [[What is list() in Python?]](./what-is-list-function-in-python.md)
* External: [https://docs.python.org/3/library/functions.html#zip](https://docs.python.org/3/library/functions.html#zip)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "What does zip() do in Python?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "zip() pairs up items from two or more lists (or any iterables) position by position. Give it [1, 2, 3] and ['a', 'b', 'c'], and you get tuples: (1, 'a'), (2, 'b'), (3, 'c'). It stops when the shortest list runs out. Perfect for iterating over multiple lists in parallel or creating dictionaries from separate key and value lists. The result is an iterator, so wrap it in list() if you need to see or reuse the full output. Think of it as a zipper joining two sides together—hence the name."
    }
  }]
}
</script>
