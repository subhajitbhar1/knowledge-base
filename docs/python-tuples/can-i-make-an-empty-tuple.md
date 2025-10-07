---
title: "Can I make an empty tuple?"
description: "Yes: empty_tuple = () or empty_tuple = tuple(). Useful for initializing before loops or as placeholders."
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

# Can I make an empty tuple?

<!-- more -->

!!! info "In short"
    Yes. Use `empty_tuple = ()` or `empty_tuple = tuple()`. Both create an empty tuple with length 0. Empty tuples are useful as default values, placeholders, or initial values before building up data. Unlike empty lists (which are mutable and can cause default argument bugs), empty tuples are safe as defaults. Note: empty parentheses `()` make an empty tuple, but empty curly braces `{}` make an empty dict, not an empty set. For an empty set, use `set()`.

Creating an empty tuple is straightforward and useful.

Just use empty parentheses or call the `tuple()` constructor.

In the following example, we create and work with empty tuples:

```python
# Two ways to create empty tuple
empty1 = ()
empty2 = tuple()

print(empty1)  # ()
print(empty2)  # ()
print(type(empty1))  # <class 'tuple'>
print(len(empty1))  # 0

# They're equal
print(empty1 == empty2)  # True

# Safe as function default
def process_data(items=()):
    if not items:
        return "No data"
    return sum(items)

print(process_data())  # "No data"
print(process_data((1, 2, 3)))  # 6

# Compare with empty list (mutable, dangerous as default)
def bad_function(items=[]):  # DON'T do this!
    items.append("surprise")
    return items

print(bad_function())  # ['surprise']
print(bad_function())  # ['surprise', 'surprise'] - Oops!

# Empty tuple is immutable, so safe
def good_function(items=()):
    return tuple(list(items) + ["added"])

print(good_function())  # ('added',)
print(good_function())  # ('added',) - Always fresh

# Building up from empty
result = ()
for i in range(3):
    result = result + (i,)  # Inefficient but works
print(result)  # (0, 1, 2)
```

Both `()` and `tuple()` create the same empty tuple. The empty tuple is safe as a default because it's immutable—every call gets the same frozen empty tuple, which can't accidentally accumulate state.

Empty tuples are less common than empty lists, but they have their uses.

## Gotchas

* **Empty dict, not empty set** — `{}` creates an empty dict. For an empty set, use `set()`. Empty tuple is `()`.
* **Building tuples is slow** — adding to tuples with `result = result + (new_item,)` creates a new tuple each time. For building, use lists and convert: `tuple(my_list)`.
* **Empty tuple is falsy** — `if my_tuple:` returns False for empty tuples. Use `if len(my_tuple) > 0:` if you need explicit checks.

## See also

* [How do you write a tuple in Python?](how-to-write-a-tuple-in-python.md)
* [What is the tuple for 5?](what-is-the-tuple-for-5.md)
* External: [https://docs.python.org/3/library/functions.html#func-tuple](https://docs.python.org/3/library/functions.html#func-tuple)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "Can I make an empty tuple?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Yes. Use empty_tuple = () or empty_tuple = tuple(). Both create an empty tuple with length 0. Empty tuples are useful as default values, placeholders, or initial values. Unlike empty lists (which can cause default argument bugs), empty tuples are safe as defaults."
    }
  }]
}
</script>
