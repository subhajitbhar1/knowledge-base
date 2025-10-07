---
title: "How do I add items to a Python list?"
description: "Learn all methods to add items to lists: append(), insert(), extend(), and concatenation with examples and performance tips."
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: Subhajit Bhar, freelance data scientist, OCR, NLP, LLM, RAG, knowledge base, python, lists, manipulation
  - name: Publisher
    content: Subhajit Bhar
date: 2025-10-07
updated: "2025-10-07"
---

# How do I add items to a Python list?

<!-- more -->

!!! info "In short"
    Most of the time, you just `.append(item)` to stick something on the end. Need it at a specific spot? `.insert(index, item)` works but pushes everything else over. Got multiple items to add? `.extend([items])` or `+=` dumps them all in at once. Want a new list instead of modifying the original? Use `+` concatenation: `new_list = old_list + [more_stuff]`. Append is your workhorse—fast, simple, does what you expect. The others exist for when append isn't enough.

Let's see each method in action:

```python
# Append single item
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)

# Insert at position
fruits.insert(1, "blueberry")
print(fruits)

# Extend with multiple items
fruits.extend(["date", "elderberry"])
print(fruits)

# Concatenation (creates new list)
more_fruits = fruits + ["fig", "grape"]
print(len(more_fruits))
```

In the example above, `append` adds "cherry" to the end, giving us `['apple', 'banana', 'cherry']`. Then `insert` squeezes "blueberry" into position 1, pushing everything else to the right. The `extend` method adds two more fruits in one go, and finally, the `+` operator creates a completely new list with 8 total items.

## Gotchas

* **append() vs extend()** — this catches everyone once. `list.append([1, 2])` adds the entire list as one nested item, while `list.extend([1, 2])` unpacks and adds 1 and 2 individually. Big difference.
* **insert() is slow** — putting something at the front (index 0) means Python has to shift everything down. For lots of insertions at the start, use `collections.deque` instead.
* **Concatenation copies** — `list1 + list2` creates a brand new list. If you just want to modify `list1`, use `list1.extend(list2)` or `list1 += list2` instead. Saves memory.

## See also

* [[What does append() mean in Python?]](./what-does-append-mean-in-python.md)
* [[How do I remove elements from a Python list?]](./how-to-remove-elements-from-list.md)
* External: [https://docs.python.org/3/tutorial/datastructures.html#more-on-lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "How do I add items to a Python list?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Most of the time, you just .append(item) to stick something on the end. Need it at a specific spot? .insert(index, item) works but pushes everything else over. Got multiple items to add? .extend([items]) or += dumps them all in at once. Want a new list instead of modifying the original? Use + concatenation: new_list = old_list + [more_stuff]. Append is your workhorse—fast, simple, does what you expect. The others exist for when append isn't enough."
    }
  }]
}
</script>
