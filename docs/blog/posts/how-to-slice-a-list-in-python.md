---
title: "How do you slice a list in Python?"
description: "Master Python list slicing: syntax, step values, negative indices, and practical patterns for extracting sublists."
tags:
  - python
  - lists
  - indexing
date: 2025-10-07
updated: "2025-10-07"
---

# How do you slice a list in Python?

<!-- more -->

!!! info "In short"
    Slicing pulls out chunks of a list with `[start:end:step]`. It includes the start position but stops *before* end. So `list[1:4]` gives you indices 1, 2, 3. Leave parts out for defaults: `[:3]` is first three, `[2:]` is everything from index 2 onward, `[:]` copies the whole thing. Negatives work: `[-3:]` grabs the last three items. The step lets you skip: `[::2]` is every other item, `[::-1]` reverses the list. Best part? Slicing never crashes—bad indices just give you an empty list or clip to what exists.

Here are some common slicing patterns:

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic slicing
print(numbers[2:5])      # [2, 3, 4]
print(numbers[:4])       # First 4
print(numbers[6:])       # From 6 to end

# With step
print(numbers[::2])      # Every other
print(numbers[1::2])     # Odd indices

# Reverse
print(numbers[::-1])
```

Running the code above, `numbers[2:5]` extracts `[2, 3, 4]`, `[:4]` gives the first four `[0, 1, 2, 3]`, and `[6:]` gets everything from 6 onward. The step parameter `[::2]` picks every other element: `[0, 2, 4, 6, 8]`. And that `[::-1]` trick reverses the entire list.

That `[::-1]` trick for reversing is a Python classic. Reads weird, works great.

## Gotchas

* **End is exclusive** — `list[0:3]` gets 0, 1, 2. Not 0, 1, 2, 3. This trips up everyone at first. Think "up to but not including."
* **Out-of-range is safe** — `list[100:200]` on a small list just gives `[]`. Unlike single indexing which crashes, slicing clips silently. Sometimes that's nice, sometimes it hides bugs.
* **Shallow copy** — `new = old[:]` copies the list structure but shares nested objects. Change a nested list in `new` and you'll see it in `old` too. For true independence, use `copy.deepcopy()`.

## See also

* [[How do you access elements in a Python list?]](./how-to-access-elements-in-list.md)
* [[What is [-1] in a Python list?]](./what-is-negative-one-in-list.md)
* External: [https://docs.python.org/3/tutorial/introduction.html#lists](https://docs.python.org/3/tutorial/introduction.html#lists)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "How do you slice a list in Python?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Slicing pulls out chunks of a list with [start:end:step]. It includes the start position but stops before end. So list[1:4] gives you indices 1, 2, 3. Leave parts out for defaults: [:3] is first three, [2:] is everything from index 2 onward, [:] copies the whole thing. Negatives work: [-3:] grabs the last three items. The step lets you skip: [::2] is every other item, [::-1] reverses the list. Best part? Slicing never crashes—bad indices just give you an empty list or clip to what exists."
    }
  }]
}
</script>
