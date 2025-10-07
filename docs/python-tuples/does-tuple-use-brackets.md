---
title: "Does a tuple use brackets?"
description: "Tuples use parentheses (), not brackets. Lists use []. But you access elements with brackets: my_tuple[0]."
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: Subhajit Bhar, freelance data scientist, OCR, NLP, LLM, RAG, knowledge base, python, tuple, syntax
  - name: Publisher
    content: Subhajit Bhar
date: 2025-10-07
updated: "2025-10-07"
---

# Does a tuple use brackets?

<!-- more -->

!!! info "In short"
    Tuples use parentheses `()` for creation, not brackets. Lists use square brackets `[]`. Dictionaries use curly braces `{}`. But here's the confusing part: you access tuple elements WITH brackets: `my_tuple[0]`. So tuples are created with `()` but accessed with `[]`. That bracket notation is for indexing—it works on any sequence (tuples, lists, strings). Creation syntax differs, but element access is consistent across all sequences. Remember: `(1, 2, 3)` creates a tuple, `my_tuple[1]` accesses its second element.

Tuples use parentheses for creation, but brackets for element access.

This can be confusing at first, but it's consistent with how Python handles all sequences.

In the following example, we see both syntaxes in use:

```python
# Creating structures - different brackets
my_tuple = (1, 2, 3)    # Parentheses for tuples
my_list = [1, 2, 3]     # Square brackets for lists
my_dict = {"a": 1}      # Curly braces for dicts
my_set = {1, 2, 3}      # Curly braces for sets

# Accessing elements - SAME brackets for sequences
print(my_tuple[0])  # 1 - brackets for access
print(my_list[0])   # 1 - brackets for access
print("hello"[0])   # 'h' - even strings use brackets

# Slicing also uses brackets
print(my_tuple[1:3])  # (2, 3)
print(my_list[1:3])   # [2, 3]

# This is NOT a tuple (just parentheses for grouping)
not_tuple = (5)
print(type(not_tuple))  # <class 'int'>

# This IS a tuple (comma makes it)
is_tuple = (5,)
print(type(is_tuple))  # <class 'tuple'>
print(is_tuple[0])  # 5 - access with brackets
```

Parentheses create tuples (with commas). Brackets access elements. Same pattern for lists, tuples, strings—all sequences use `[]` for indexing.

The brackets are for the indexing operation, not the data type definition.

## Gotchas

* **Parentheses for grouping** — `(5)` is just the number 5 in parens. `(5,)` is a tuple. The comma matters more than the parentheses.
* **Tuple unpacking uses no brackets** — `a, b, c = my_tuple` doesn't need brackets on the left side.
* **Bracket means "get item"** — whether it's `my_tuple[0]`, `my_list[0]`, or `my_dict["key"]`, brackets mean "give me this element."

## See also

* [How do you write a tuple in Python?](how-to-write-a-tuple-in-python.md)
* [What is the tuple for 5?](what-is-the-tuple-for-5.md)
* External: [https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "Does a tuple use brackets?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Tuples use parentheses () for creation, not brackets. Lists use square brackets []. But you access tuple elements WITH brackets: my_tuple[0]. So tuples are created with () but accessed with []. Creation syntax differs, but element access is consistent across all sequences."
    }
  }]
}
</script>
