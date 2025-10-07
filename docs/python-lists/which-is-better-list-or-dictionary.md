---
title: "Which is better — list or dictionary in Python?"
description: "Neither is universally better. Learn the trade-offs and decision criteria for choosing lists vs dictionaries."
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: Subhajit Bhar, freelance data scientist, OCR, NLP, LLM, RAG, knowledge base, python, lists, comparison
  - name: Publisher
    content: Subhajit Bhar
date: 2025-10-07
updated: "2025-10-07"
---

# Which is better — list or dictionary in Python?

<!-- more -->

!!! info "In short"
    Neither. They're tools for different jobs. Lists are for ordered sequences you access by position. Dicts are for data you look up by unique keys. It's like asking "which is better, a screwdriver or a hammer?" Lists are simpler and lighter for small collections. Dicts give you O(1) lookups instead of O(n). The real question: are you asking "what's at position 5?" (list) or "what's the value for this ID/name?" (dict). Match your data structure to your access pattern, not abstract notions of "better."

Let me show you when each fits:

```python
# List: position-based, ordered processing
tasks = ["Write code", "Test code", "Deploy"]
for i, task in enumerate(tasks, 1):
    print(f"{i}. {task}")

print("---")

# Dict: lookup by identifier
employees = {
    "E001": "Alice",
    "E002": "Bob",
    "E003": "Carol"
}
print(f"Employee E002: {employees['E002']}")

# Combining both is fine
task_status = {"Write code": "done", "Test code": "in progress"}
print(task_status.get("Test code"))
```

In the code above, the list naturally fits numbered tasks: "1. Write code", "2. Test code", "3. Deploy". The dict makes employee lookup instant—we ask for "E002" and get "Bob". And that last line shows you can mix approaches: a dict of task statuses works great.

See? Different access patterns, different structures. Use what fits the question you're asking.

## Gotchas

* **Access pattern decides** — if you're iterating with `for item in collection:`, either works. But if you're doing `collection[key]` repeatedly, you want a dict.
* **You can combine them** — lists of dicts, dicts of lists—both are perfectly valid when you need both structures. Don't overthink it.
* **Small data doesn't matter** — for <100 items, performance differences are negligible. Pick what reads clearest to you and future maintainers.

## See also

* [Are lists or dictionaries faster in Python?](are-lists-or-dictionaries-faster.md)
* [When to use list vs tuple vs dictionary vs set in Python?](list-vs-tuple-vs-dictionary-vs-set.md)
* External: [https://docs.python.org/3/tutorial/datastructures.html](https://docs.python.org/3/tutorial/datastructures.html)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "Which is better — list or dictionary in Python?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Neither. They're tools for different jobs. Lists are for ordered sequences you access by position. Dicts are for data you look up by unique keys. It's like asking which is better, a screwdriver or a hammer? Lists are simpler and lighter for small collections. Dicts give you O(1) lookups instead of O(n). The real question: are you asking what's at position 5? (list) or what's the value for this ID/name? (dict). Match your data structure to your access pattern, not abstract notions of better."
    }
  }]
}
</script>
