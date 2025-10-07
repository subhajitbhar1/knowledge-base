---
title: "What is slicing in Python?"
description: "Slicing extracts portions using [start:stop:step]. Works on tuples, lists, strings. Returns a new sequence."
meta:
  - name: robots
    content: index: follow
  - name: keywords
    content: Subhajit Bhar, freelance data scientist, OCR, NLP, LLM, RAG, knowledge base, python, tuple, indexing
  - name: Publisher
    content: Subhajit Bhar
date: 2025-10-07
updated: "2025-10-07"
---

# What is slicing in Python?

<!-- more -->

!!! info "In short"
    Slicing extracts a portion of a sequence using bracket notation: `my_tuple[start:stop:step]`. `start` is inclusive, `stop` is exclusive. `my_tuple[1:4]` gives elements at indices 1, 2, 3 (not 4). Omit values to use defaults: `[:3]` means "from beginning to index 3", `[2:]` means "from index 2 to end", `[::2]` means "every second element". Works on tuples, lists, and strings. Always returns a new sequence—the original is unchanged. Negative indices work too: `[-3:]` gives last 3 elements. Slicing is how you extract subsets without loops.

Slicing uses `[start:stop:step]` syntax to extract portions of sequences.

It's one of Python's most useful features for working with ordered data.

In the following example, we see slicing in action:

```python
my_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Basic slice [start:stop]
print(my_tuple[2:5])  # (2, 3, 4) - indices 2, 3, 4

# From beginning
print(my_tuple[:4])  # (0, 1, 2, 3)

# To end
print(my_tuple[6:])  # (6, 7, 8, 9)

# With step [start:stop:step]
print(my_tuple[1:8:2])  # (1, 3, 5, 7) - every 2nd element

# Every second element
print(my_tuple[::2])  # (0, 2, 4, 6, 8)

# Reverse
print(my_tuple[::-1])  # (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)

# Negative indices (last 3)
print(my_tuple[-3:])  # (7, 8, 9)

# Copy entire tuple
copy = my_tuple[:]
print(copy == my_tuple)  # True
print(copy is my_tuple)  # True for tuples (immutable)
```

Each slice creates a new tuple (or for tuples, sometimes returns the same immutable object). The syntax `[start:stop:step]` is flexible—omit any part for defaults.

Slicing never modifies the original—it always returns a new sequence.

## Gotchas

* **Stop is exclusive** — `my_tuple[0:3]` gives indices 0, 1, 2. Not 3. This trips people up constantly.
* **Out of range is fine** — `my_tuple[5:100]` just gives from index 5 to the end. No error. Python handles it gracefully.
* **Step can't be zero** — `my_tuple[::0]` raises `ValueError`. Step must be non-zero.

## See also

* [How do you access elements in a Python list?](../python-lists/how-to-access-elements-in-list.md)
* [What is [-1] in a Python list?](../python-lists/what-is-negative-one-in-list.md)
* External: [https://docs.python.org/3/tutorial/introduction.html#lists](https://docs.python.org/3/tutorial/introduction.html#lists)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "What is slicing in Python?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Slicing extracts a portion of a sequence using bracket notation: my_tuple[start:stop:step]. start is inclusive, stop is exclusive. Works on tuples, lists, and strings. Always returns a new sequence. Negative indices work too. Slicing is how you extract subsets without loops."
    }
  }]
}
</script>
