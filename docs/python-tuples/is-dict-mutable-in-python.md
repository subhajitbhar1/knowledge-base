---
title: "Is dict mutable in Python?"
description: "Yes, dictionaries are mutable. You can add, remove, and change key-value pairs after creation."
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

# Is dict mutable in Python?

<!-- more -->

!!! info "In short"
    Yes, dictionaries are completely mutable. You can add new keys, delete existing ones, update values, even clear the entire dict. This makes them flexible for dynamic data but means they can't be used as dict keys or set members (not hashable). Dict keys must be immutable (strings, numbers, tuples), but values can be anything, including other dicts or lists. The mutability lets you build complex nested structures and modify them freely. If you need an immutable dict-like structure, check out `types.MappingProxyType` for read-only dict views.

Dictionaries are mutable—you can modify them freely after creation.

Just like lists, dicts can grow, shrink, and change.

In the following example, we demonstrate dict mutability:

```python
# Create a dict
person = {"name": "Alice", "age": 30}
print(person)

# Add new key-value pair
person["email"] = "alice@example.com"
print(person)

# Modify existing value
person["age"] = 31
print(person)

# Delete a key
del person["email"]
print(person)

# Update multiple at once
person.update({"city": "NYC", "age": 32})
print(person)

# Clear everything
person.clear()
print(person)  # {}

# Dicts can't be dict keys (not hashable)
try:
    nested = {person: "value"}
except TypeError as e:
    print(f"Error: {e}")

# But tuples can (if they contain only immutables)
key_tuple = ("name", "age")
valid_dict = {key_tuple: "metadata"}
print(valid_dict)
```

The dict accepts all modifications—additions, changes, deletions. But trying to use a dict as a key fails because mutable objects aren't hashable.

That mutability is what makes dicts powerful for dynamic data structures.

## Gotchas

* **Keys must be immutable** — you can't use lists or dicts as keys. Tuples work, but only if they contain immutable items.
* **Dict values can be anything** — mutable or immutable. `{"key": [1, 2, 3]}` is fine.
* **Shared references** — `dict2 = dict1` creates a reference, not a copy. Modify one, both change. Use `dict2 = dict1.copy()` for independence.

## See also

* [Are tuples immutable?](are-tuples-immutable.md)
* [What cannot have duplicates in Python?](what-cannot-have-duplicates-in-python.md)
* External: [https://docs.python.org/3/tutorial/datastructures.html#dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "Is dict mutable in Python?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Yes, dictionaries are completely mutable. You can add new keys, delete existing ones, update values, even clear the entire dict. This makes them flexible for dynamic data but means they can't be used as dict keys or set members (not hashable). Dict keys must be immutable, but values can be anything."
    }
  }]
}
</script>
