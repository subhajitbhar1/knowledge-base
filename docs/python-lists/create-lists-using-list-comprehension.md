---
title: "How do you create lists using list comprehension?"
description: "Master Python list comprehensions: syntax, filtering, nested loops, and when this concise pattern beats traditional loops."
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: Subhajit Bhar, freelance data scientist, OCR, NLP, LLM, RAG, knowledge base, python, lists, comprehension
  - name: Publisher
    content: Subhajit Bhar
date: 2025-10-07
updated: "2025-10-07"
---

# How do you create lists using list comprehension?

<!-- more -->

!!! info "In short"
    List comprehensions let you build lists in one elegant line: `[expression for item in iterable]`. Want to filter? Add `if` at the end: `[x for x in range(10) if x % 2 == 0]`. They're faster than manually looping with `.append()` and way more readable for simple operations. You can even nest them for 2D structures: `[[x*y for x in range(3)] for y in range(3)]`. But here's the rule: if it doesn't fit comfortably on one line, use a regular loop. Comprehensions are about clarity, not code golf.

Let's see comprehensions in action:

```python
# Basic comprehension
squares = [x**2 for x in range(5)]

# With condition
evens = [x for x in range(10) if x % 2 == 0]

# Transform strings
names = ["alice", "bob"]
capitalized = [name.upper() for name in names]

# Nested comprehension (2D)
matrix = [[i+j for j in range(3)] for i in range(3)]

print(squares)
print(evens)
print(matrix)
```

In the code above, the first comprehension gives us `[0, 1, 4, 9, 16]`. The filtered version produces `[0, 2, 4, 6, 8]`. And that nested one creates a 2D matrix: `[[0, 1, 2], [1, 2, 3], [2, 3, 4]]`.

The nested one reads a bit backwards—outer loop first, then inner. Takes getting used to.

## Gotchas

* **Don't get clever** — if you need to squint to understand your comprehension, it's too complex. Use a regular loop. Readability beats brevity.
* **The if-else dance** — you can't write `[x if x > 0 for x in items]`. It needs to be `[x if x > 0 else 0 for x in items]` or `[x for x in items if x > 0]`. The first replaces fails, the second filters them out.
* **Nested comprehensions read weird** — `[x for row in matrix for x in row]` flattens a 2D list. But the loops read inside-out compared to regular for loops. Takes practice.

## See also

* [When to use a list comprehension in Python?](when-to-use-list-comprehension-in-python.md)
* [How do you create a list in Python?](how-to-create-list-in-python.md)
* External: [https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "How do you create lists using list comprehension?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "List comprehensions let you build lists in one elegant line: [expression for item in iterable]. Want to filter? Add if at the end: [x for x in range(10) if x % 2 == 0]. They're faster than manually looping with .append() and way more readable for simple operations. You can even nest them for 2D structures: [[x*y for x in range(3)] for y in range(3)]. But here's the rule: if it doesn't fit comfortably on one line, use a regular loop. Comprehensions are about clarity, not code golf."
    }
  }]
}
</script>
