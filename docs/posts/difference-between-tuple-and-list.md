---
title: "What is the difference between a tuple and a list?"
description: "Compare Python tuples and lists: mutability, syntax, performance, and when to use each data structure in your code."
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: Subhajit Bhar, freelance data scientist, OCR, NLP, LLM, RAG, knowledge base, python, lists, comparison
  - name: Publisher
    content: Subhajit Bhar
date: 2025-10-07
updated: "2025-10-07"
---

# What is the difference between a tuple and a list?

<!-- more -->

!!! info "In short"
    The big one? Lists can change, tuples can't. Lists use square brackets `[]`, tuples use parentheses `()`. Once you create a tuple, it's frozen—no adding, removing, or modifying items. Lists are your go-to for collections that evolve. Tuples signal "this data is fixed"—like coordinates (x, y) or RGB colors. Tuples are slightly faster and use less memory, but honestly, for small stuff the difference is tiny. The real reason to pick tuples? You *mean* the data shouldn't change. Plus, tuples can be dictionary keys; lists can't.

Let's see the difference in action:

```python
# List (mutable)
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)

# Tuple (immutable)
my_tuple = (1, 2, 3)
# my_tuple.append(4)  # AttributeError!
print(my_tuple)
print(type(my_tuple))
```

In the code above, the list happily accepts a new item with `append`. But if you uncomment that tuple line, Python crashes with an error—tuples don't have an `append` method because they can't be modified. The output shows `[1, 2, 3, 4]` for the list and `(1, 2, 3)` for the unchanged tuple.

Here's the weird bit: `(1)` isn't a tuple, it's just an integer. You need a comma: `(1,)`. This catches everyone once.

## Gotchas

* **Single-item tuple needs a comma** — writing `(1)` just gives you the number 1 wrapped in parens. Write `(1,)` to make Python treat it as a tuple. Silly rule, but you'll remember after it bites you once.
* **Tuples aren't fully immutable** — if your tuple contains a list, you can still modify that list. The tuple's structure is locked, but mutable objects inside aren't magically frozen.
* **Performance is overrated** — yes, tuples are a hair faster. But for most code, readability and intent matter more. Choose tuples when you want to say "don't touch this data", not to squeeze out microseconds.

## See also

* [[When would you use a tuple instead of a list?]](./when-to-use-tuple-instead-of-list.md)
* [[When to use list vs tuple vs dictionary vs set in Python?]](./list-vs-tuple-vs-dictionary-vs-set.md)
* External: [https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "What is the difference between a tuple and a list?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "The big one? Lists can change, tuples can't. Lists use square brackets [], tuples use parentheses (). Once you create a tuple, it's frozen—no adding, removing, or modifying items. Lists are your go-to for collections that evolve. Tuples signal this data is fixed—like coordinates (x, y) or RGB colors. Tuples are slightly faster and use less memory, but honestly, for small stuff the difference is tiny. The real reason to pick tuples? You mean the data shouldn't change. Plus, tuples can be dictionary keys; lists can't."
    }
  }]
}
</script>
