---
title: "What is the difference between a tuple and a list?"
description: "Tuples are immutable and use (), lists are mutable and use []. Learn performance and use case differences."
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: Subhajit Bhar, freelance data scientist, OCR, NLP, LLM, RAG, knowledge base, python, tuple, comparison
  - name: Publisher
    content: Subhajit Bhar
date: 2025-10-07
updated: "2025-10-07"
---

# What is the difference between a tuple and a list?

<!-- more -->

!!! info "In short"
    The big one: tuples can't be changed (immutable), lists can (mutable). Tuples use parentheses `(1, 2, 3)`, lists use brackets `[1, 2, 3]`. Because tuples are immutable, they're hashable—you can use them as dict keys and set members. Lists can't do that. Tuples are slightly faster and use less memory. Lists have more methods (append, remove, etc.). Use tuples for fixed data like coordinates or function returns. Use lists for collections you'll modify. Tuples signal "this structure won't change." Lists signal "this is a working collection."

Mutability is the core difference—everything else flows from that.

Tuples are frozen. Lists are flexible.

In the following example, we compare their behavior side-by-side:

```python
# Creation syntax
my_tuple = (1, 2, 3)
my_list = [1, 2, 3]

# Modification
my_list[0] = 99  # Works fine
print(my_list)  # [99, 2, 3]

try:
    my_tuple[0] = 99  # Fails
except TypeError as e:
    print(f"Tuple error: {e}")

# Adding elements
my_list.append(4)
print(my_list)  # [99, 2, 3, 4]

# Tuples can't append (no method exists)
print(dir(my_tuple))  # No append, remove, etc.

# Hashability
print(hash(my_tuple))  # Works - tuples are hashable
try:
    print(hash(my_list))  # Fails
except TypeError as e:
    print(f"List error: {e}")

# Dict keys
my_dict = {my_tuple: "value"}  # Works
# my_dict = {my_list: "value"}  # Would fail
```

The list cheerfully modifies. The tuple refuses. The list can't be hashed. The tuple can be a dict key.

Those constraints define when you use each.

## Gotchas

* **Conversion is easy** — `list(my_tuple)` and `tuple(my_list)` convert between them. Useful when you need mutability or immutability temporarily.
* **Performance difference is minor** — for small collections (<1000 items), the speed difference is negligible. Choose for semantics, not micro-optimization.
* **Both keep order** — lists and tuples both maintain insertion order. Sets don't guarantee order (though modern Python preserves it).

## See also

* [What are the main differences between list and tuple in Python?](main-differences-between-list-and-tuple.md)
* [What are the advantages of a tuple over a list?](advantages-of-tuple-over-list.md)
* External: [https://docs.python.org/3/tutorial/datastructures.html](https://docs.python.org/3/tutorial/datastructures.html)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "What is the difference between a tuple and a list?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "The big one: tuples can't be changed (immutable), lists can (mutable). Tuples use parentheses (1, 2, 3), lists use brackets [1, 2, 3]. Because tuples are immutable, they're hashable—you can use them as dict keys and set members. Lists can't do that. Tuples are slightly faster and use less memory."
    }
  }]
}
</script>
