---
title: "Which of the following is a Python tuple (4 5 6 4 5 6 4 5 6 {})?"
description: "Only (4, 5, 6) is a valid tuple. Learn to identify tuple syntax with parentheses and commas."
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

# Which of the following is a Python tuple (4 5 6 4 5 6 4 5 6 {})?

<!-- more -->

!!! info "In short"
    From those options, only expressions with parentheses and commas are tuples: `(4, 5, 6)` is a tuple. `4 5 6` is a syntax error. `{}` is an empty dict, not a tuple. To identify tuples: look for comma-separated values, usually in parentheses. `(1, 2)`, `(x,)`, or even just `1, 2` (without parens) are tuples. Square brackets `[4, 5, 6]` make a list. Curly braces with colons `{key: value}` make a dict. Curly braces with just values `{1, 2}` make a set. Parentheses with commas? That's your tuple.

Let's clarify tuple syntax by testing different forms:

```python
# Valid tuple
tuple1 = (4, 5, 6)
print(type(tuple1))  # <class 'tuple'>
print(tuple1)  # (4, 5, 6)

# Tuple without parentheses (valid!)
tuple2 = 4, 5, 6
print(type(tuple2))  # <class 'tuple'>

# NOT a tuple - syntax error
try:
    invalid = 4 5 6
except SyntaxError:
    print("4 5 6 is invalid syntax")

# Empty braces = dict, not tuple
empty_dict = {}
print(type(empty_dict))  # <class 'dict'>

# Empty tuple needs parentheses
empty_tuple = ()
print(type(empty_tuple))  # <class 'tuple'>

# List (square brackets)
my_list = [4, 5, 6]
print(type(my_list))  # <class 'list'>

# Set (curly braces, no colons)
my_set = {4, 5, 6}
print(type(my_set))  # <class 'set'>
```

Only the first two are tuples. `4 5 6` without commas or structure is invalid Python. `{}` creates an empty dict. `()` creates an empty tuple.

The comma is what makes a tuple—parentheses just make it clearer.

## Gotchas

* **Empty structures** — `()` is an empty tuple, `[]` is an empty list, `{}` is an empty dict (not set!). To make an empty set, use `set()`.
* **Single-element confusion** — `(4)` is just `4`. Write `(4,)` for a single-element tuple.
* **Commas matter more than parentheses** — `x = 1, 2` creates a tuple. Parentheses are for grouping and clarity, not requirement (except empty tuples).

## See also

* [How do you write a tuple in Python?](how-to-write-a-tuple-in-python.md)
* [Does a tuple use brackets?](does-tuple-use-brackets.md)
* External: [https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "Which of the following is a Python tuple?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Only expressions with parentheses and commas are tuples: (4, 5, 6) is a tuple. 4 5 6 is a syntax error. {} is an empty dict, not a tuple. To identify tuples: look for comma-separated values, usually in parentheses."
    }
  }]
}
</script>
