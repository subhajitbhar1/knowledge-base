---
title: "What cannot have duplicates in Python?"
description: "Sets and dictionary keys can't have duplicates. Tuples and lists can. Learn which structure fits your needs."
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

# What cannot have duplicates in Python?

<!-- more -->

!!! info "In short"
    Sets and dictionary keys cannot have duplicates—Python automatically removes them. Add `2` to a set twice? You'll only see it once. Try to create a dict with duplicate keys? The last value wins. Lists and tuples, on the other hand, happily keep duplicates. That's the trade-off: sets give you automatic uniqueness and O(1) membership testing, but lose order (pre-3.7) and allow only hashable items. Need uniqueness? Use a set. Need to preserve every element including dupes? Use a list or tuple.

Sets and dictionary keys enforce uniqueness automatically.

If you try to add duplicates, Python silently removes them (sets) or overwrites them (dicts).

In the following example, we see how different structures handle duplicates:

```python
# Sets automatically remove duplicates
my_set = {1, 2, 2, 3, 2}
print(my_set)  # {1, 2, 3}

my_set.add(2)  # Try adding 2 again
print(my_set)  # {1, 2, 3} - still only one 2

# Dictionary keys can't duplicate
my_dict = {'a': 1, 'b': 2, 'a': 3}
print(my_dict)  # {'a': 3, 'b': 2} - last 'a' wins

# Lists and tuples CAN have duplicates
my_list = [1, 2, 2, 3, 2]
print(my_list)  # [1, 2, 2, 3, 2]

my_tuple = (1, 2, 2, 3, 2)
print(my_tuple)  # (1, 2, 2, 3, 2)
```

The set collapses to `{1, 2, 3}`. The dict keeps only the last value for duplicate key `'a'`. But the list and tuple preserve all the `2`s.

That automatic deduplication makes sets perfect when you need unique values.

## Gotchas

* **Insertion order in sets** — modern Python (3.7+) preserves insertion order in dicts but sets still don't guarantee order reliably. Don't depend on set order.
* **Converting to remove dupes** — `unique_list = list(set(my_list))` is a common pattern to deduplicate, but it loses order. Use `dict.fromkeys(my_list)` if order matters.
* **Dict values CAN duplicate** — only keys must be unique. Multiple keys can have the same value: `{'a': 1, 'b': 1}` is fine.

## See also

* [Can tuples have duplicates?](can-tuples-have-duplicates.md)
* [What is the difference between a tuple and a list?](difference-between-tuple-and-list.md)
* External: [https://docs.python.org/3/tutorial/datastructures.html#sets](https://docs.python.org/3/tutorial/datastructures.html#sets)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "What cannot have duplicates in Python?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Sets and dictionary keys cannot have duplicates—Python automatically removes them. Add 2 to a set twice? You'll only see it once. Try to create a dict with duplicate keys? The last value wins. Lists and tuples, on the other hand, happily keep duplicates."
    }
  }]
}
</script>
