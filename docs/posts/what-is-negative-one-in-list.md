---
title: "What is [-1] in a Python list?"
description: "Understand negative indexing in Python: how [-1] accesses the last element and why it's a powerful shorthand."
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: Subhajit Bhar, freelance data scientist, OCR, NLP, LLM, RAG, knowledge base, python, lists, indexing
  - name: Publisher
    content: Subhajit Bhar
date: 2025-10-07
updated: "2025-10-07"
---

# What is [-1] in a Python list?

<!-- more -->

!!! info "In short"
    `[-1]` grabs the last item in the list. Simple as that. Negative indices count from the end: `-1` is last, `-2` is second-to-last, and so on. It's way cleaner than writing `list[len(list) - 1]` every time you need the last element. Works on any sequence—lists, tuples, strings, whatever. Empty list? You'll get an `IndexError`, same as with regular indices. But for non-empty lists, `[-1]` is your quick shortcut to "give me the last thing."

Let me show you negative indexing in action:

```python
# Negative indexing
numbers = [10, 20, 30, 40, 50]

print(numbers[-1])   # Last element
print(numbers[-2])   # Second to last
print(numbers[-5])   # First element (same as [0])

# Works on strings too
text = "Hello"
print(text[-1])      

# Last element without knowing length
last = numbers[-1]
print(f"Last: {last}")
```

In the code above, `numbers[-1]` gives us `50`, `numbers[-2]` gives `40`, and `numbers[-5]` reaches all the way back to the first element, `10`. It even works on strings—`text[-1]` returns `'o'`.

Notice `-5` gets you the first element. Count backwards from the end: -1, -2, -3, -4, -5.

## Gotchas

* **Empty list crashes** — `[][-1]` raises IndexError. There's no last element to grab. If you're unsure the list has items, check `if my_list:` first or use slicing: `my_list[-1:]` returns `[]` safely.
* **Still out-of-bounds errors** — `list[-1000]` on a small list crashes. Negative indexing doesn't magically protect you from bad indices, it just changes which direction you're counting.
* **Slicing vs indexing** — in slices, `list[:-1]` means "everything *except* the last element." That's different from accessing `list[-1]`. Takes a moment to internalize.

## See also

* [[How do you access elements in a Python list?]](./how-to-access-elements-in-list.md)
* [[How do you slice a list in Python?]](./how-to-slice-a-list-in-python.md)
* External: [https://docs.python.org/3/tutorial/introduction.html#lists](https://docs.python.org/3/tutorial/introduction.html#lists)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "What is [-1] in a Python list?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "[-1] grabs the last item in the list. Simple as that. Negative indices count from the end: -1 is last, -2 is second-to-last, and so on. It's way cleaner than writing list[len(list) - 1] every time you need the last element. Works on any sequence—lists, tuples, strings, whatever. Empty list? You'll get an IndexError, same as with regular indices. But for non-empty lists, [-1] is your quick shortcut to give me the last thing."
    }
  }]
}
</script>
