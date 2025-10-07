---
title: "What is a tuple in Python?"
description: "Learn what Python tuples are, how they differ from lists, and why immutability matters for your code."
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

# What is a tuple in Python?

<!-- more -->

!!! info "In short"
    A tuple is Python's immutable sibling to the list. Same ordered sequence idea, but once you create it, it's locked—no adding, removing, or changing elements. You write them with parentheses: `(1, 2, 3)` instead of `[1, 2, 3]`. That immutability is the whole point. Use tuples when you want to protect data from accidental changes, return multiple values from functions, or use sequences as dictionary keys. They're faster and lighter than lists, but the real win is signaling intent: "this data structure is fixed."

A tuple is an ordered collection that can't be modified after creation.

Think of it as a list that's been sealed shut. You can read from it, loop through it, but you can't change what's inside.

In the following example, we create a tuple and try to modify it:

```python
# Creating a tuple
coordinates = (10, 20)
print(coordinates)
print(type(coordinates))

# Accessing works fine
print(f"X: {coordinates[0]}, Y: {coordinates[1]}")

# But modification fails
try:
    coordinates[0] = 15
except TypeError as e:
    print(f"Error: {e}")
```

Running this code prints `(10, 20)` and `<class 'tuple'>`, then shows the error: `'tuple' object does not support item assignment`. That's immutability at work—tuples refuse changes.

The parentheses and immutability are what make tuples distinct from lists.

## Gotchas

* **Parentheses are optional** — `x = 1, 2, 3` creates a tuple too. The comma makes it a tuple, not the parentheses. But use parentheses for clarity.
* **Single-item tuple needs comma** — `(5)` is just an int. Write `(5,)` for a one-element tuple. That trailing comma is required.
* **Immutability is shallow** — if your tuple contains a list, that list can still be modified. The tuple's structure is frozen, but mutable objects inside aren't protected.

## See also

* [Are tuples immutable?](are-tuples-immutable.md)
* [What is the difference between a tuple and a list?](difference-between-tuple-and-list.md)
* External: [https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "What is a tuple in Python?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "A tuple is Python's immutable sibling to the list. Same ordered sequence idea, but once you create it, it's locked—no adding, removing, or changing elements. You write them with parentheses: (1, 2, 3) instead of [1, 2, 3]. That immutability is the whole point. Use tuples when you want to protect data from accidental changes, return multiple values from functions, or use sequences as dictionary keys. They're faster and lighter than lists, but the real win is signaling intent: this data structure is fixed."
    }
  }]
}
</script>
