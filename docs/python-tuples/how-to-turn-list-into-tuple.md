---
title: "How do I turn a list into a tuple?"
description: "Use tuple(my_list) to convert any list to a tuple. Simple, fast, and creates an immutable copy."
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: Subhajit Bhar, freelance data scientist, OCR, NLP, LLM, RAG, knowledge base, python, tuple, conversion
  - name: Publisher
    content: Subhajit Bhar
date: 2025-10-07
updated: "2025-10-07"
---

# How do I turn a list into a tuple?

<!-- more -->

!!! info "In short"
    Just wrap it in `tuple()`: `my_tuple = tuple(my_list)`. Done. This creates an immutable copy with the same elements in the same order. The original list stays unchanged. Why convert? To use as a dict key, pass to a function that expects immutability, or freeze data you don't want modified. Conversion is fast for small lists, but remember: if your list contains mutable objects (like other lists), those inner objects stay mutable. The tuple structure is frozen, but nested mutables aren't magically protected.

Call `tuple()` with your list as the argument.

That's it. Python creates a new tuple with the same elements.

In the following example, we convert lists to tuples and see how they behave:

```python
# Basic conversion
my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)
print(my_tuple)  # (1, 2, 3, 4)
print(type(my_tuple))  # <class 'tuple'>

# Original list unchanged
my_list.append(5)
print(my_list)  # [1, 2, 3, 4, 5]
print(my_tuple)  # (1, 2, 3, 4) - unchanged

# Use case: dictionary key
coordinates_list = [10, 20]
# Can't use list as dict key
# my_dict = {coordinates_list: "point A"}  # TypeError

# But tuple works
coordinates_tuple = tuple(coordinates_list)
my_dict = {coordinates_tuple: "point A"}
print(my_dict[(10, 20)])  # "point A"
```

The conversion creates `(1, 2, 3, 4)` from `[1, 2, 3, 4]`. Changes to the list don't affect the tuple—they're separate objects. The dict key example shows why you'd convert: lists can't be keys, but tuples can.

That's the main reason to convert: unlock hashability.

## Gotchas

* **Shallow copy** — `tuple(my_list)` copies the list structure, but if the list contains other lists, those inner lists are still mutable and shared.
* **Empty and single-element** — `tuple([])` gives `()`. `tuple([5])` gives `(5,)` with the trailing comma automatically handled.
* **Performance** — converting huge lists (millions of elements) takes time and memory. If you're doing it in a hot loop, reconsider your design.

## See also

* [Can I convert a tuple to a list in Python?](convert-tuple-to-list.md)
* [What is the difference between a tuple and a list?](difference-between-tuple-and-list.md)
* External: [https://docs.python.org/3/library/functions.html#func-tuple](https://docs.python.org/3/library/functions.html#func-tuple)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "How do I turn a list into a tuple?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Just wrap it in tuple(): my_tuple = tuple(my_list). Done. This creates an immutable copy with the same elements in the same order. The original list stays unchanged. Why convert? To use as a dict key, pass to a function that expects immutability, or freeze data you don't want modified."
    }
  }]
}
</script>
