---
title: "What is a Python list?"
description: "Learn exactly what Python lists are, how they store data, and why they're the most versatile built-in data structure for ordered collections."
tags:
  - python
  - lists
  - basics
date: 2025-10-07
updated: "2025-10-07"
---

# What is a Python list?

<!-- more -->

!!! info "In short"
    Think of a list as your quick storage shelf for keeping multiple things together. It's just square brackets with items inside, separated by commas. The beauty? You can change it anytime—add stuff, remove stuff, rearrange it. Lists remember the order you put things in, and you can grab any item by its position (starting from 0, which trips everyone up at first). They're mutable, ordered, and don't care if you mix types. When you need a flexible collection that grows and shrinks, reach for a list.

Here's a quick example showing what you can do with lists:

```python
# Create a list with mixed types
my_list = [1, "apple", 3.14, True, [5, 6]]

# Access elements by index
print(my_list[0])      # First element
print(my_list[-1])     # Last element

# Modify the list
my_list.append("new")
print(len(my_list))
```

In the code above, notice how we can mix numbers, strings, and even other lists. The first `print` gives us `1`, the second shows `[5, 6]` (negative indices count from the end), and after appending, the length becomes `6`.

Here's what catches people: lists are mutable. Pass one to a function and it can change your original list without warning. That's powerful but also a common source of bugs.

## Gotchas

* **Lists share references** — when you write `list2 = list1`, you're not copying. Both names point to the same list. Changes to one affect the other. Use `list2 = list1.copy()` when you need independence.
* **Searching is slow** — checking `if item in my_list` walks through every element. For big lists, that's painful. If you're doing lots of lookups, a set or dictionary will save you.
* **Zero-based indexing bites beginners** — the first item is `my_list[0]`, not `my_list[1]`. It feels weird until it doesn't.

## See also

* [[Python Lists Overview]](../index.md)
* [[How do you create a list in Python?]](./how-to-create-list-in-python.md)
* External: [https://docs.python.org/3/tutorial/datastructures.html](https://docs.python.org/3/tutorial/datastructures.html)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "What is a Python list?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Think of a list as your quick storage shelf for keeping multiple things together. It's just square brackets with items inside, separated by commas. The beauty? You can change it anytime—add stuff, remove stuff, rearrange it. Lists remember the order you put things in, and you can grab any item by its position (starting from 0, which trips everyone up at first). They're mutable, ordered, and don't care if you mix types. When you need a flexible collection that grows and shrinks, reach for a list."
    }
  }]
}
</script>
