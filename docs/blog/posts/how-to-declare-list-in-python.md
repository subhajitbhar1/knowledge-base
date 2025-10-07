---
title: "How do I declare a list in Python?"
description: "Learn the correct syntax for declaring lists in Python, from empty lists to pre-populated collections with type hints."
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: Subhajit Bhar, freelance data scientist, OCR, NLP, LLM, RAG, knowledge base, python, lists, creation
  - name: Publisher
    content: Subhajit Bhar
date: 2025-10-07
updated: "2025-10-07"
---

# How do I declare a list in Python?

<!-- more -->

!!! info "In short"
    Python doesn't do declarations like Java or C. You just... make the list. Write `my_list = [1, 2, 3]` and you're done. Want an empty one? `my_list = []`. That's it. The act of assigning creates the list—no separate declaration step. If you're into type hints (optional but increasingly popular), you can write `my_list: list[int] = []` to signal "this will hold integers." But Python won't enforce that at runtime. It's documentation for you and your IDE, not a strict rule.

Here's how "declaration" works in Python:

```python
# Basic declaration (assignment)
numbers = [1, 2, 3, 4, 5]

# Empty list declaration
items = []

# With type hints (optional)
names: list[str] = ["Alice", "Bob"]

# Verify they're all lists
print(type(numbers))
print(type(items))
print(names)
```

Running this code shows that all three approaches produce proper list objects. The output displays `<class 'list'>` for both `numbers` and `items`, and `['Alice', 'Bob']` for the names list.

The confusion usually comes from other languages where you declare *then* assign. Python merges those into one step.

## Gotchas

* **No var/let/const keywords** — if you're coming from JavaScript, forget `let` and `const`. Python just uses the variable name directly. It feels weird for about five minutes.
* **Type hints are optional** — they're great for readability and catching bugs with tools like mypy, but Python won't stop you from putting strings in a `list[int]`. They're hints, not contracts.
* **Old vs new syntax** — Python 3.9+ uses lowercase `list[int]`. Earlier versions needed `from typing import List` then `List[int]` (capital L). Modern code prefers the simpler lowercase version.

## See also

* [[How do you create a list in Python?]](./how-to-create-list-in-python.md)
* [[How do I start or initialize a list in Python?]](./how-to-initialize-list-in-python.md)
* External: [https://docs.python.org/3/library/typing.html](https://docs.python.org/3/library/typing.html)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "How do I declare a list in Python?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Python doesn't do declarations like Java or C. You just... make the list. Write my_list = [1, 2, 3] and you're done. Want an empty one? my_list = []. That's it. The act of assigning creates the list—no separate declaration step. If you're into type hints (optional but increasingly popular), you can write my_list: list[int] = [] to signal this will hold integers. But Python won't enforce that at runtime. It's documentation for you and your IDE, not a strict rule."
    }
  }]
}
</script>
