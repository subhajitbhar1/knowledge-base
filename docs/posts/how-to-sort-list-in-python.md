---
title: "How do I sort a list in Python?"
description: "Master Python list sorting: sort() vs sorted(), reverse order, custom keys, and performance considerations for ordering lists."
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: Subhajit Bhar, freelance data scientist, OCR, NLP, LLM, RAG, knowledge base, python, lists, sorting
  - name: Publisher
    content: Subhajit Bhar
date: 2025-10-07
updated: "2025-10-07"
---

# How do I sort a list in Python?

<!-- more -->

!!! info "In short"
    Two ways: `.sort()` modifies your list in-place (and returns nothing), while `sorted(list)` gives you a new sorted list and leaves the original alone. Both default to ascending order. Want descending? Add `reverse=True`. Need custom sorting, like by length? Use the `key` parameter: `.sort(key=len)`. Python's sort is seriously fast—it uses Timsort, which is optimized for real-world data and runs in O(n log n). For most cases, just call `.sort()` and move on. It's stable too, meaning equal items keep their original order.

Let me show you both approaches:

```python
# In-place sorting
numbers = [3, 1, 4, 1, 5]
numbers.sort()
print(numbers)

# Create new sorted list
original = [3, 1, 4]
sorted_copy = sorted(original)
print(f"Original: {original}, Sorted: {sorted_copy}")

# Reverse and custom key
words = ["apple", "pie", "a", "cherry"]
words.sort(key=len, reverse=True)
print(words)
```

In the code above, `numbers.sort()` modifies the list to `[1, 1, 3, 4, 5]`. The `sorted()` function creates a new list `[1, 3, 4]` while leaving `original` as `[3, 1, 4]`. That last example sorts by string length in descending order, giving us `['cherry', 'apple', 'pie', 'a']`.

That key parameter is powerful—you can sort by anything: string length, last character, whatever.

## Gotchas

* **sort() returns None** — writing `result = my_list.sort()` makes `result` None. The sorting happens to the list itself. This is intentional Python design to prevent confusion about whether you got a new list or modified the old one.
* **Can't sort mixed types** — `[1, "two", 3].sort()` crashes in Python 3. Everything needs to be comparable. Strings compare to strings, numbers to numbers, but not across types.
* **Key functions open up power** — `key=str.lower` for case-insensitive sorting, `key=lambda x: x[1]` to sort tuples by their second element. Once you get comfortable with key functions, you'll use them everywhere.

## See also

* [[What is a Python list?]](./what-is-a-python-list.md)
* [[How do I add items to a Python list?]](./how-to-add-items-to-list.md)
* External: [https://docs.python.org/3/howto/sorting.html](https://docs.python.org/3/howto/sorting.html)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "How do I sort a list in Python?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Two ways: .sort() modifies your list in-place (and returns nothing), while sorted(list) gives you a new sorted list and leaves the original alone. Both default to ascending order. Want descending? Add reverse=True. Need custom sorting, like by length? Use the key parameter: .sort(key=len). Python's sort is seriously fast—it uses Timsort, which is optimized for real-world data and runs in O(n log n). For most cases, just call .sort() and move on. It's stable too, meaning equal items keep their original order."
    }
  }]
}
</script>
