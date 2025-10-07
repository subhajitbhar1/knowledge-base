---
title: "How do shallow and deep copies work in Python lists?"
description: "Master list copying: shallow vs deep copies, when each is needed, and how to avoid reference bugs with nested lists."
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: Subhajit Bhar, freelance data scientist, OCR, NLP, LLM, RAG, knowledge base, python, lists, copy
  - name: Publisher
    content: Subhajit Bhar
date: 2025-10-07
updated: "2025-10-07"
---

# How do shallow and deep copies work in Python lists?

<!-- more -->

!!! info "In short"
    Shallow copy creates a new list but shares the objects inside—use `list.copy()`, `list[:]`, or `list(original)`. Deep copy recursively copies everything, including nested objects—use `copy.deepcopy()`. For simple lists of immutable stuff (numbers, strings), shallow is fine and fast. But for lists containing mutable objects (other lists, dicts), shallow copies share those inner objects—change one, see it in both. Deep copies are slower but give true independence. Most of the time shallow is enough. Reach for deep only when you have nested structures and need full separation.

Let me show you the critical difference:

```python
import copy

# Shallow copy: inner lists are shared
original = [[1, 2], [3, 4]]
shallow = original.copy()
shallow[0][0] = 99  # Modifies original too!
print(f"Original: {original}")
print(f"Shallow: {shallow}")

print("---")

# Deep copy: completely independent
original2 = [[1, 2], [3, 4]]
deep = copy.deepcopy(original2)
deep[0][0] = 99
print(f"Original2: {original2}")
print(f"Deep: {deep}")
```

Running this code, the shallow copy shows `[[99, 2], [3, 4]]` for both original and copy—the inner lists are shared! But the deep copy keeps `original2` as `[[1, 2], [3, 4]]` while only `deep` becomes `[[99, 2], [3, 4]]`. Complete independence.

See how the shallow copy's change bled through to the original? That's the gotcha.

## Gotchas

* **Assignment isn't copying** — `list2 = list1` creates a reference, not a copy. Both names point to the same list. Always use `.copy()` when you want independence.
* **Shallow fails with nesting** — for 2D lists, shallow copy only copies the outer list. The inner lists are still shared. This catches people constantly.
* **Deep copy is expensive** — it traverses and copies everything recursively. For huge nested structures, this can be slow and memory-hungry. Use only when you truly need it.

## See also

* [What is a Python list?](what-is-a-python-list.md)
* [How does list mutability affect performance?](list-mutability-and-performance.md)
* External: [https://docs.python.org/3/library/copy.html](https://docs.python.org/3/library/copy.html)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "How do shallow and deep copies work in Python lists?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Shallow copy creates a new list but shares the objects inside—use list.copy(), list[:], or list(original). Deep copy recursively copies everything, including nested objects—use copy.deepcopy(). For simple lists of immutable stuff (numbers, strings), shallow is fine and fast. But for lists containing mutable objects (other lists, dicts), shallow copies share those inner objects—change one, see it in both. Deep copies are slower but give true independence. Most of the time shallow is enough. Reach for deep only when you have nested structures and need full separation."
    }
  }]
}
</script>
