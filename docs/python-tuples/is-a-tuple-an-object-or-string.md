---
title: "Is a tuple an object or a string?"
description: "A tuple is an object - specifically, an immutable sequence object. Everything in Python is an object."
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: Subhajit Bhar, freelance data scientist, OCR, NLP, LLM, RAG, knowledge base, python, tuple, concepts
  - name: Publisher
    content: Subhajit Bhar
date: 2025-10-07
updated: "2025-10-07"
---

# Is a tuple an object or a string?

<!-- more -->

!!! info "In short"
    A tuple is an object—specifically, an instance of the `tuple` class. Everything in Python is an object: numbers, strings, functions, even classes themselves. Strings are also objects, but they're instances of the `str` class. So a tuple isn't a string, it's a different type of object. When you write `(1, 2, 3)`, Python creates a tuple object in memory with type `<class 'tuple'>`. The confusion might come from seeing tuples printed as strings, but that's just the string representation of the tuple object. Objects and strings are not mutually exclusive—strings ARE objects too.

A tuple is an object. More precisely, it's an instance of Python's built-in `tuple` class.

Everything in Python is an object, including strings. So the question creates a false dichotomy—strings are objects too.

Here's how to check what something is:

```python
my_tuple = (1, 2, 3)
my_string = "hello"

# Check types
print(type(my_tuple))  # <class 'tuple'>
print(type(my_string))  # <class 'str'>

# Both are objects
print(isinstance(my_tuple, object))  # True
print(isinstance(my_string, object))  # True

# But they're different types
print(isinstance(my_tuple, tuple))  # True
print(isinstance(my_tuple, str))  # False

# String representation of a tuple
tuple_as_string = str(my_tuple)
print(tuple_as_string)  # "(1, 2, 3)"
print(type(tuple_as_string))  # <class 'str'>
```

Both show `True` for `isinstance(..., object)` because everything inherits from `object`. But they're different specific types: `tuple` vs `str`.

When you print a tuple, Python converts it to a string representation. But the tuple itself isn't a string.

## Gotchas

* **Everything is an object** — in Python, literally everything is an object. Numbers, booleans, functions, modules, classes. Object-oriented all the way down.
* **String representation** — `str(my_tuple)` converts a tuple to its string form. But that's not the same as the tuple being a string.
* **Type vs instance** — `tuple` is a type (class). `(1, 2, 3)` is an instance (object) of that type.

## See also

* [What is a tuple in Python?](what-is-a-tuple-in-python.md)
* [What is called a tuple in Python?](what-is-called-a-tuple-in-python.md)
* External: [https://docs.python.org/3/reference/datamodel.html#objects-values-and-types](https://docs.python.org/3/reference/datamodel.html#objects-values-and-types)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "Is a tuple an object or a string?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "A tuple is an object—specifically, an instance of the tuple class. Everything in Python is an object: numbers, strings, functions, even classes themselves. Strings are also objects, but they're instances of the str class. So a tuple isn't a string, it's a different type of object."
    }
  }]
}
</script>
