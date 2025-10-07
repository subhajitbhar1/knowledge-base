---
title: "What is called a tuple in Python?"
description: "Understand tuple terminology, syntax, and what makes this data structure unique in Python."
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: Subhajit Bhar, freelance data scientist, OCR, NLP, LLM, RAG, knowledge base, python, tuple, basics
  - name: Publisher
    content: Subhajit Bhar
date: 2025-10-07
updated: "2025-10-07"
---

# What is called a tuple in Python?

<!-- more -->

!!! info "In short"
    The term "tuple" refers to an immutable, ordered sequence in Python. It's called a tuple (rhymes with "couple") because it groups multiple values into a single unit. Mathematically, tuples come from set theory—ordered pairs, triples, n-tuples. In Python, a tuple is any comma-separated sequence, usually wrapped in parentheses: `(1, 2, 3)`. The name tuple is the general term; specific sizes have names too: pair (2 elements), triple (3), quadruple (4). But in Python code, we just say "tuple" regardless of size.

A tuple is what Python calls its built-in immutable sequence type.

The word tuple comes from mathematics, where it means an ordered collection of elements. Python borrowed the name and the concept.

Here's what gets called a tuple in Python:

```python
# All of these are tuples
coordinates = (10, 20)  # pair
rgb_color = (255, 128, 0)  # triple
empty = ()  # empty tuple
single = (42,)  # single-element tuple

# Even without parentheses, commas make tuples
also_tuple = 1, 2, 3
print(type(also_tuple))  # <class 'tuple'>

# Not a tuple
just_int = (42)  # parentheses without comma = just an int
print(type(just_int))  # <class 'int'>
```

The type shows `<class 'tuple'>` for all the actual tuples. The last one is just an int because there's no comma.

The commas are what create the tuple, not the parentheses. But we use parentheses for clarity.

## Gotchas

* **Pronunciation** — some say "TOO-pull," others say "TUP-pull." Both are correct. Python doesn't care.
* **Tuple packing** — `x = 1, 2, 3` is called "tuple packing" because you're packing values into a tuple.
* **Tuple unpacking** — `a, b, c = x` is "unpacking" because you're extracting values from a tuple. Useful terminology to know.

## See also

* [What is a tuple in Python?](what-is-a-tuple-in-python.md)
* [How do you write a tuple in Python?](how-to-write-a-tuple-in-python.md)
* External: [https://docs.python.org/3/library/stdtypes.html#tuples](https://docs.python.org/3/library/stdtypes.html#tuples)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "What is called a tuple in Python?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "The term tuple refers to an immutable, ordered sequence in Python. It's called a tuple (rhymes with couple) because it groups multiple values into a single unit. Mathematically, tuples come from set theory—ordered pairs, triples, n-tuples. In Python, a tuple is any comma-separated sequence, usually wrapped in parentheses: (1, 2, 3)."
    }
  }]
}
</script>
