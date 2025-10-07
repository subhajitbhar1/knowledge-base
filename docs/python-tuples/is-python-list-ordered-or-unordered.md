---
title: "Is Python list ordered or unordered?"
description: "Lists are ordered. They maintain insertion order and support indexing. Sets are unordered."
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

# Is Python list ordered or unordered?

<!-- more -->

!!! info "In short"
    Lists are ordered. They remember the exact sequence you added items in and maintain that order. `[3, 1, 2]` stays `[3, 1, 2]` until you explicitly change it. You can access elements by position: `my_list[0]` always gives the first element. Tuples are also ordered. Dicts preserve insertion order (Python 3.7+). Sets are the unordered ones—they don't guarantee any particular sequence. If order matters, use lists or tuples. If you just need membership testing and don't care about sequence, use sets.

Lists are fully ordered collections.

They maintain insertion order and let you access elements by numeric index.

In the following example, we see how lists preserve order:

```python
# Order is maintained
my_list = [3, 1, 4, 1, 5]
print(my_list)  # [3, 1, 4, 1, 5]

# Add more - order still preserved
my_list.append(9)
print(my_list)  # [3, 1, 4, 1, 5, 9]

# Access by position
print(f"First: {my_list[0]}")  # 3
print(f"Last: {my_list[-1]}")  # 9

# Slicing maintains order
print(my_list[1:4])  # [1, 4, 1]

# Compare with set (unordered)
my_set = {3, 1, 4, 1, 5}
print(my_set)  # {1, 3, 4, 5} - duplicates removed, order may differ

# Can't index into a set
try:
    print(my_set[0])
except TypeError as e:
    print(f"Set error: {e}")
```

The list keeps `[3, 1, 4, 1, 5, 9]` exactly as added. The set removes duplicates and doesn't support indexing.

Order is a defining feature of lists and tuples.

## Gotchas

* **Sorting changes order** — `my_list.sort()` rearranges elements. But that's explicit—lists don't reorder on their own.
* **Dicts are ordered now** — Python 3.7+ dicts maintain insertion order too. But that's relatively recent (pre-3.7 dicts were unordered).
* **Sets have no index** — you can't do `my_set[0]`. Sets are for membership testing, not positional access.

## See also

* [Does tuple keep order in Python?](does-tuple-keep-order-in-python.md)
* [What cannot have duplicates in Python?](what-cannot-have-duplicates-in-python.md)
* External: [https://docs.python.org/3/tutorial/datastructures.html](https://docs.python.org/3/tutorial/datastructures.html)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "Is Python list ordered or unordered?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Lists are ordered. They remember the exact sequence you added items in and maintain that order. You can access elements by position. Tuples are also ordered. Dicts preserve insertion order (Python 3.7+). Sets are the unordered ones—they don't guarantee any particular sequence."
    }
  }]
}
</script>
