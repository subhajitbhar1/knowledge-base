---
title: "How do you write a tuple in Python?"
description: "Use parentheses with commas: (1, 2, 3). For single items, add trailing comma: (1,). Parentheses are optional but recommended."
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: Subhajit Bhar, freelance data scientist, OCR, NLP, LLM, RAG, knowledge base, python, tuple, creation
  - name: Publisher
    content: Subhajit Bhar
date: 2025-10-07
updated: "2025-10-07"
---

# How do you write a tuple in Python?

<!-- more -->

!!! info "In short"
    Write tuples with parentheses and commas: `(1, 2, 3)`. The comma is what creates the tuple—parentheses just make it clear. You can omit them: `x = 1, 2, 3` is valid but less readable. For single-element tuples, the trailing comma is mandatory: `(5,)` not `(5)`. Empty tuples need parentheses: `()`. Tuples can hold any types, mixed or uniform: `(1, "text", 3.14, [1, 2])` works fine. The syntax is simple, but that single-element comma trips everyone up at least once.

The basic syntax is parentheses with commas separating values.

But there are several valid forms and important edge cases.

Here's how to write tuples correctly:

```python
# Standard tuple
my_tuple = (1, 2, 3)
print(my_tuple)  # (1, 2, 3)

# Without parentheses (valid, but less clear)
also_tuple = 1, 2, 3
print(also_tuple)  # (1, 2, 3)
print(type(also_tuple))  # <class 'tuple'>

# Single-element tuple (comma is REQUIRED)
single = (5,)
print(single)  # (5,)
print(len(single))  # 1

# Without comma, it's just the value
not_tuple = (5)
print(type(not_tuple))  # <class 'int'>

# Empty tuple
empty = ()
print(empty)  # ()

# Mixed types (perfectly fine)
mixed = (1, "hello", 3.14, [1, 2], {"key": "value"})
print(mixed)

# Nested tuples
nested = ((1, 2), (3, 4), (5, 6))
print(nested)

# Trailing comma in multi-element (optional, but helps with diffs)
with_trailing = (
    1,
    2,
    3,
)
print(with_trailing)  # (1, 2, 3)
```

The standard form `(1, 2, 3)` is clearest. The single-element `(5,)` is the gotcha. The comma-only form `1, 2, 3` works but is less obvious.

Stick to parentheses for clarity, but know the comma is what matters.

## Gotchas

* **Single-element trap** — `(x)` is just `x`. Write `(x,)`. This is the #1 tuple gotcha. Test with `len()` if unsure.
* **Tuple unpacking** — `a, b, c = (1, 2, 3)` works without parens on the right: `a, b, c = 1, 2, 3` is equivalent.
* **Generator vs tuple** — `(x for x in range(5))` is a generator expression, not a tuple. Use `tuple(x for x in range(5))` to get a tuple.

## See also

* [What is the tuple for 5?](what-is-the-tuple-for-5.md)
* [Can I make an empty tuple?](can-i-make-an-empty-tuple.md)
* External: [https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "How do you write a tuple in Python?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Write tuples with parentheses and commas: (1, 2, 3). The comma is what creates the tuple—parentheses just make it clear. For single-element tuples, the trailing comma is mandatory: (5,) not (5). Empty tuples need parentheses: (). Tuples can hold any types, mixed or uniform."
    }
  }]
}
</script>
