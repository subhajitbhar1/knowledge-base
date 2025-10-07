---
title: "Can I convert a tuple to a list in Python?"
description: "Yes: my_list = list(my_tuple). Creates a mutable copy you can modify without affecting the original."
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

# Can I convert a tuple to a list in Python?

<!-- more -->

!!! info "In short"
    Yes. Use `my_list = list(my_tuple)`. This creates a new mutable list with the same elements. The original tuple stays unchanged—they're separate objects. Why convert? When you need to add, remove, or modify elements. Lists have `.append()`, `.remove()`, `.sort()`, etc. Tuples don't. Convert when you need mutability. Common pattern: receive a tuple, convert to list for processing, optionally convert back to tuple for return. The conversion is fast for small sequences, but remember: it's a shallow copy. If the tuple contains mutable objects, those are shared.

Call `list()` with your tuple as the argument.

Simple, fast, and creates an independent mutable copy.

In the following example, we convert tuples to lists and see how they behave:

```python
# Basic conversion
my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)

print(my_tuple)  # (1, 2, 3, 4, 5)
print(my_list)   # [1, 2, 3, 4, 5]
print(type(my_list))  # <class 'list'>

# Now you can modify the list
my_list.append(6)
my_list.remove(2)
my_list[0] = 99

print(my_list)   # [99, 1, 3, 4, 5, 6]
print(my_tuple)  # (1, 2, 3, 4, 5) - unchanged

# Common pattern: process and convert back
def process_data(data_tuple):
    # Convert to list for modification
    data_list = list(data_tuple)
    
    # Process
    data_list.sort()
    data_list.append(max(data_list) + 1)
    
    # Convert back to tuple
    return tuple(data_list)

result = process_data((5, 2, 8, 1))
print(result)  # (1, 2, 5, 8, 9)

# Empty tuple converts to empty list
empty_list = list(())
print(empty_list)  # []
```

The list() constructor creates `[1, 2, 3, 4, 5]` from `(1, 2, 3, 4, 5)`. Modifications to the list don't affect the tuple—they're separate objects.

That independence is key: converting gives you a mutable workspace.

## Gotchas

* **Shallow copy** — `list(my_tuple)` copies the tuple structure, but if elements are mutable (like nested lists), those are shared between tuple and list.
* **Performance** — for huge tuples (millions of elements), conversion takes time and memory. Don't convert unnecessarily in tight loops.
* **Why not just use list initially?** — sometimes you receive tuples from libraries, database drivers, or function returns. You don't choose the type, so you convert.

## See also

* [How do I turn a list into a tuple?](how-to-turn-list-into-tuple.md)
* [What does the tuple() function do?](what-does-tuple-function-do.md)
* External: [https://docs.python.org/3/library/functions.html#func-list](https://docs.python.org/3/library/functions.html#func-list)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "Can I convert a tuple to a list in Python?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Yes. Use my_list = list(my_tuple). This creates a new mutable list with the same elements. The original tuple stays unchanged. Why convert? When you need to add, remove, or modify elements. Lists have append, remove, sort methods. Tuples don't."
    }
  }]
}
</script>
