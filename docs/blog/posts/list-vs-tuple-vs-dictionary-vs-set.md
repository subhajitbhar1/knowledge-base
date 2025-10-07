---
title: "When to use list vs tuple vs dictionary vs set in Python?"
description: "Complete comparison guide: choose the right Python data structure based on mutability, order, uniqueness, and access patterns."
tags:
  - python
  - lists
  - comparison
date: 2025-10-07
updated: "2025-10-07"
---

# When to use list vs tuple vs dictionary vs set in Python?

<!-- more -->

!!! info "In short"
    **Lists** for ordered, changeable sequences (your default). **Tuples** for fixed structures that shouldn't change. **Dicts** for key-value lookups. **Sets** for unique items with fast membership tests. Lists and tuples keep order; sets don't (though dicts do now in 3.7+). Lists and dicts are mutable; tuples are immutable. Ask yourself: Need order? Can it change? Looking up by key? Must items be unique? One question usually makes the choice obvious. When in doubt, start with a list and refactor if needed.

Here's each structure in action:

```python
# List: ordered, mutable, duplicates OK
tasks = ["code", "test", "deploy", "test"]
tasks.append("monitor")
print(f"List: {tasks}")

# Tuple: immutable structure
point = (10, 20, 30)
print(f"Tuple: {point}")

# Dict: key-value lookup
config = {"host": "localhost", "port": 8080}
print(f"Dict port: {config['port']}")

# Set: unique items, fast membership
tags = {"python", "coding", "python"}  # Dup removed
print(f"Set: {tags}")
print(f"'python' in set: {'python' in tags}")
```

Running this shows how each behaves: the list keeps duplicates `['code', 'test', 'deploy', 'test', 'monitor']`, the tuple stays fixed at `(10, 20, 30)`, the dict provides instant lookup with `8080`, and the set automatically deduplicates to `{'coding', 'python'}`.

Each has its lane. Use the right tool for the job.

## Gotchas

* **Sets lose order** — don't rely on iteration order for sets, even though they technically maintain insertion order in modern Python. Use lists or dicts when order matters to your logic.
* **Tuples for groups, lists for collections** — use tuples for heterogeneous fixed-size data (coordinates, return values), lists for variable-size homogeneous sequences.
* **Dict keys must be hashable** — lists can't be dict keys, tuples can. That's a big practical difference.

## See also

* [[What is the difference between a tuple and a list?]](./difference-between-tuple-and-list.md)
* [[Which is better — list or dictionary in Python?]](./which-is-better-list-or-dictionary.md)
* External: [https://docs.python.org/3/tutorial/datastructures.html](https://docs.python.org/3/tutorial/datastructures.html)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "When to use list vs tuple vs dictionary vs set in Python?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Lists for ordered, changeable sequences (your default). Tuples for fixed structures that shouldn't change. Dicts for key-value lookups. Sets for unique items with fast membership tests. Lists and tuples keep order; sets don't (though dicts do now in 3.7+). Lists and dicts are mutable; tuples are immutable. Ask yourself: Need order? Can it change? Looking up by key? Must items be unique? One question usually makes the choice obvious. When in doubt, start with a list and refactor if needed."
    }
  }]
}
</script>
