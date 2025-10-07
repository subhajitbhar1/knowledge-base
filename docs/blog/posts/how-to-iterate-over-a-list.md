---
title: "How do you iterate over a list in Python?"
description: "Learn all methods for looping through lists: for loops, while loops, enumerate, comprehensions, and iterator patterns."
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: Subhajit Bhar, freelance data scientist, OCR, NLP, LLM, RAG, knowledge base, python, lists, loops
  - name: Publisher
    content: Subhajit Bhar
date: 2025-10-07
updated: "2025-10-07"
---

# How do you iterate over a list in Python?

<!-- more -->

!!! info "In short"
    The Python way: `for item in my_list:`. Clean, readable, does what it says. Need the index too? `for i, item in enumerate(my_list):` gives you both. Only reach for while loops if you need to skip ahead or jump around dynamically. Coming from other languages, you might want to write `for i in range(len(my_list)):` but that's un-Pythonic—iterate over items directly. For processing and transforming, list comprehensions often read better: `[process(x) for x in my_list]`. Simple patterns work best.

Here are the main ways to loop through a list:

```python
fruits = ["apple", "banana", "cherry"]

# Basic iteration
for fruit in fruits:
    print(fruit)

print("---")

# With index
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

print("---")

# While loop (less common)
i = 0
while i < len(fruits):
    print(fruits[i].upper())
    i += 1
```

In the above example, the basic loop prints each fruit on its own line. The `enumerate()` version gives us numbered output: "0: apple", "1: banana", "2: cherry". And the while loop (which you'll rarely need) prints uppercased versions.

See how the `enumerate()` version is cleaner than manually tracking an index variable.

## Gotchas

* **Don't modify while iterating** — `for item in list: list.remove(item)` is a classic bug. The iterator gets confused as the list shrinks. Use a comprehension: `list = [x for x in list if keep(x)]`.
* **Avoid range(len())** — `for i in range(len(list)):` works but screams "I learned Python yesterday." Iterate directly over items or use `enumerate()` when you need indices.
* **Iterators exhaust** — if you convert to an iterator with `iter()`, you can only loop once. Lists themselves are iterable (not iterators) so you can loop multiple times safely.

## See also

* [[What does zip() do in Python?]](./what-does-zip-do-in-python.md)
* [[How do you create lists using list comprehension?]](./create-lists-using-list-comprehension.md)
* External: [https://docs.python.org/3/tutorial/datastructures.html#looping-techniques](https://docs.python.org/3/tutorial/datastructures.html#looping-techniques)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "How do you iterate over a list in Python?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "The Python way: for item in my_list:. Clean, readable, does what it says. Need the index too? for i, item in enumerate(my_list): gives you both. Only reach for while loops if you need to skip ahead or jump around dynamically. Coming from other languages, you might want to write for i in range(len(my_list)): but that's un-Pythonic—iterate over items directly. For processing and transforming, list comprehensions often read better: [process(x) for x in my_list]. Simple patterns work best."
    }
  }]
}
</script>
