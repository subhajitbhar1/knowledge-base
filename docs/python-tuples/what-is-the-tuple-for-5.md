---
title: "What is the tuple for 5?"
description: "A single-element tuple for 5 is (5,). Learn why the trailing comma is required and common gotchas."
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: Subhajit Bhar, freelance data scientist, OCR, NLP, LLM, RAG, knowledge base, python, tuple, examples
  - name: Publisher
    content: Subhajit Bhar
date: 2025-10-07
updated: "2025-10-07"
---

# What is the tuple for 5?

<!-- more -->

!!! info "In short"
    The tuple for 5 is `(5,)` with a trailing comma. Without the comma, `(5)` is just the integer 5 in parentheses—Python sees it as grouping, not a tuple. That trailing comma tells Python "this is a one-element tuple, not just a number." Weird syntax, but it prevents ambiguity. Once you have two or more elements, the comma between them is enough: `(5, 6)` works fine. But single-element tuples need that explicit comma. It's a quirk everyone learns once and remembers forever.

To create a single-element tuple containing 5, you write `(5,)`.

The trailing comma is mandatory. Without it, Python interprets `(5)` as just the number 5.

Here's the difference in action:

```python
# Not a tuple - just an int in parentheses
not_tuple = (5)
print(type(not_tuple))  # <class 'int'>
print(not_tuple)  # 5

# This IS a tuple
actual_tuple = (5,)
print(type(actual_tuple))  # <class 'tuple'>
print(actual_tuple)  # (5,)
print(len(actual_tuple))  # 1

# You can also omit parentheses
also_tuple = 5,
print(type(also_tuple))  # <class 'tuple'>
```

The first one is just `5`. The second is `(5,)` with length 1. The comma makes all the difference.

That trailing comma looks odd, but it's the only way Python can distinguish between a tuple and a parenthesized expression.

## Gotchas

* **Common mistake** — writing `(x)` when you mean `(x,)`. This bites everyone at least once. The code runs, but you get an int/string/whatever instead of a tuple.
* **Tuple unpacking fails** — if you try to unpack `(5)` like `a, = (5)`, you'll get an error. It only works if it's actually a tuple: `a, = (5,)`.
* **Parentheses are optional** — `5,` is valid and creates a tuple. But `(5,)` is clearer and more conventional.

## See also

* [How do you write a tuple in Python?](how-to-write-a-tuple-in-python.md)
* [Can I make an empty tuple?](can-i-make-an-empty-tuple.md)
* External: [https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "What is the tuple for 5?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "The tuple for 5 is (5,) with a trailing comma. Without the comma, (5) is just the integer 5 in parentheses—Python sees it as grouping, not a tuple. That trailing comma tells Python this is a one-element tuple, not just a number."
    }
  }]
}
</script>
