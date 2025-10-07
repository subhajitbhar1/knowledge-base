---
title: "Are tuples immutable?"
description: "Yes, tuples are immutable. Once created, you can't change, add, or remove elements. Learn why this matters."
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: Subhajit Bhar, freelance data scientist, OCR, NLP, LLM, RAG, knowledge base, python, tuple, properties
  - name: Publisher
    content: Subhajit Bhar
date: 2025-10-07
updated: "2025-10-07"
---

# Are tuples immutable?

<!-- more -->

!!! info "In short"
    Yes. Tuples are completely immutable. Once you create a tuple, you cannot add elements, remove elements, or change what's at any position. No append, no pop, no item assignment. This is the defining feature of tuples—they're frozen sequences. That immutability is what makes them hashable (usable as dict keys and set members), faster than lists, and safer for passing around without fear of modification. If you need to "change" a tuple, you create a new one. Immutability is the whole point of tuples.

Tuples are immutable, meaning they cannot be modified after creation.

Every attempt to change a tuple fails with an error.

Here's what immutability means in practice:

```python
my_tuple = (1, 2, 3)

# Can't change elements
try:
    my_tuple[0] = 99
except TypeError as e:
    print(f"Can't assign: {e}")

# Can't add elements
try:
    my_tuple.append(4)
except AttributeError as e:
    print(f"No append: {e}")

# Can't remove elements
try:
    my_tuple.remove(2)
except AttributeError as e:
    print(f"No remove: {e}")

# What you CAN do: create a new tuple
new_tuple = my_tuple + (4,)
print(new_tuple)  # (1, 2, 3, 4)
print(my_tuple)  # (1, 2, 3) - original unchanged
```

Every modification attempt fails. The only way to get a "changed" tuple is to create a new one using concatenation or other operations.

That immutability is why tuples are used for fixed data like coordinates, RGB values, or database records.

## Gotchas

* **Immutability is shallow** — if your tuple contains a list, that list can still be modified: `t = ([1, 2], 3)` allows `t[0].append(3)`. The tuple's structure is frozen, but mutable contents aren't.
* **Tuples are hashable** — because they're immutable, you can use them as dict keys and add them to sets. Lists can't do this.
* **Memory efficiency** — immutable objects can be optimized by Python. Tuples use less memory than equivalent lists.

## See also

* [What is a tuple in Python?](what-is-a-tuple-in-python.md)
* [What are the advantages of a tuple over a list?](advantages-of-tuple-over-list.md)
* External: [https://docs.python.org/3/glossary.html#term-immutable](https://docs.python.org/3/glossary.html#term-immutable)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "Are tuples immutable?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Yes. Tuples are completely immutable. Once you create a tuple, you cannot add elements, remove elements, or change what's at any position. No append, no pop, no item assignment. This is the defining feature of tuples—they're frozen sequences. That immutability is what makes them hashable, faster than lists, and safer for passing around."
    }
  }]
}
</script>
