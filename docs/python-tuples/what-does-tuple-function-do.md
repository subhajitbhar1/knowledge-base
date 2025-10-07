---
title: "What does the tuple() function do?"
description: "tuple() converts any iterable to a tuple. Use it to freeze lists, strings, or ranges into immutable sequences."
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: Subhajit Bhar, freelance data scientist, OCR, NLP, LLM, RAG, knowledge base, python, tuple, functions
  - name: Publisher
    content: Subhajit Bhar
date: 2025-10-07
updated: "2025-10-07"
---

# What does the tuple() function do?

<!-- more -->

!!! info "In short"
    `tuple()` converts any iterable into a tuple. Pass it a list, string, range, set—anything you can loop over—and you get back an immutable tuple with those elements. `tuple([1, 2, 3])` gives `(1, 2, 3)`. `tuple("hello")` gives `('h', 'e', 'l', 'l', 'o')`. Called with no arguments, `tuple()` creates an empty tuple. It's how you freeze mutable sequences or convert other iterables when you need immutability, want to use something as a dict key, or need to pass data to code expecting tuples.

The `tuple()` function creates a tuple from any iterable object.

It's the constructor for the tuple type, similar to how `list()` creates lists or `str()` creates strings.

In the following example, we convert different iterables to tuples:

```python
# From list
my_list = [1, 2, 3]
t1 = tuple(my_list)
print(t1)  # (1, 2, 3)

# From string (splits into characters)
t2 = tuple("hello")
print(t2)  # ('h', 'e', 'l', 'l', 'o')

# From range
t3 = tuple(range(5))
print(t3)  # (0, 1, 2, 3, 4)

# From set (loses order guarantees)
my_set = {3, 1, 2}
t4 = tuple(my_set)
print(t4)  # Could be (1, 2, 3) or other order

# Empty tuple
t5 = tuple()
print(t5)  # ()

# Already a tuple? Returns a copy
t6 = tuple((1, 2, 3))
print(t6)  # (1, 2, 3)
```

Each conversion creates a new tuple. Strings become tuples of characters. Ranges expand to their values. Sets get frozen into tuple form.

The function accepts any iterable—if you can loop over it, you can tuple-ify it.

## Gotchas

* **Strings become character tuples** — `tuple("hi")` gives `('h', 'i')`, not `("hi",)`. If you want a single-string tuple, use `("hi",)`.
* **Sets lose order** — converting a set to tuple gives you the elements, but order isn't guaranteed (though Python 3.7+ preserves insertion order in practice).
* **Performance** — for huge iterables, `tuple()` has to walk through every element. It's O(n) in the length of the iterable.

## See also

* [How do I turn a list into a tuple?](how-to-turn-list-into-tuple.md)
* [Can I convert a tuple to a list in Python?](convert-tuple-to-list.md)
* External: [https://docs.python.org/3/library/functions.html#func-tuple](https://docs.python.org/3/library/functions.html#func-tuple)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "What does the tuple() function do?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "tuple() converts any iterable into a tuple. Pass it a list, string, range, set—anything you can loop over—and you get back an immutable tuple with those elements. Called with no arguments, tuple() creates an empty tuple."
    }
  }]
}
</script>
