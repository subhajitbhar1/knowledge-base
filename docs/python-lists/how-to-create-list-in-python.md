---
title: "How do you create a list in Python?"
description: "Master all methods for creating Python lists: literals, constructors, comprehensions, and converting from other data types."
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: Subhajit Bhar, freelance data scientist, OCR, NLP, LLM, RAG, knowledge base, python, lists, creation
  - name: Publisher
    content: Subhajit Bhar
date: 2025-10-07
updated: "2025-10-07"
---

# How do you create a list in Python?

<!-- more -->

!!! info "In short"
    The simplest way? Just write square brackets with stuff inside: `[1, 2, 3]`. For an empty list, use `[]` or `list()`. Need to convert something else into a list? Wrap it: `list("abc")` turns a string into `['a', 'b', 'c']`. Want to generate values programmatically? List comprehensions are your friend: `[x*2 for x in range(5)]`. You can even use multiplication for repeating items: `[0] * 10` gives you ten zeros. All roads lead to the same destination—a `list` object ready to use.

Here are all the common ways to create lists:

```python
# Literal syntax
fruits = ["apple", "banana", "cherry"]

# Empty list
empty = []

# From other iterables
from_string = list("hello")
from_range = list(range(5))

# List comprehension
squares = [x**2 for x in range(5)]

print(fruits)
print(from_string)
print(squares)
```

In the above example, we create lists five different ways. The string "hello" becomes `['h', 'e', 'l', 'l', 'o']`, the range becomes `[0, 1, 2, 3, 4]`, and the comprehension gives us `[0, 1, 4, 9, 16]`.

Watch out for the repetition trick though—it has a gotcha with nested structures.

## Gotchas

* **Repetition with nested lists breaks** — writing `[[]] * 3` creates three *references* to the same inner list. Change one, change all. Use `[[] for _ in range(3)]` instead to get independent lists.
* **list() is optional** — calling `list()` with no arguments gives you `[]`. The bracket syntax is more common and clearer. Save `list()` for when you're converting something.
* **Strings explode into characters** — `list("cat")` becomes `['c', 'a', 't']`. If you wanted a list containing the string, write `["cat"]` instead. Easy to mix up.

## See also

* [How do I declare a list in Python?](how-to-declare-list-in-python.md)
* [How do I start or initialize a list in Python?](how-to-initialize-list-in-python.md)
* External: [https://docs.python.org/3/tutorial/datastructures.html#more-on-lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "How do you create a list in Python?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "The simplest way? Just write square brackets with stuff inside: [1, 2, 3]. For an empty list, use [] or list(). Need to convert something else into a list? Wrap it: list('abc') turns a string into ['a', 'b', 'c']. Want to generate values programmatically? List comprehensions are your friend: [x*2 for x in range(5)]. You can even use multiplication for repeating items: [0] * 10 gives you ten zeros. All roads lead to the same destination—a list object ready to use."
    }
  }]
}
</script>
