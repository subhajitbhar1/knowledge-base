---
title: "In what situations are lists preferred over dictionaries?"
description: "Learn when to choose lists instead of dictionaries: ordered processing, index access, and sequential data scenarios."
tags:
  - python
  - lists
  - use-cases
date: 2025-10-07
updated: "2025-10-07"
---

# In what situations are lists preferred over dictionaries?
<!-- more -->

!!! info "In short"
    Pick lists when position matters more than identity. You're processing items in order? List. Accessing by numeric index like "give me the 5th item"? List. You don't have natural keys for lookup? List. They're perfect for sequences (time-series, ordered steps, history), collecting loop results, and when all items are the same type. Lists are simpler and lighter when you don't need the key-value relationship. If you find yourself iterating through all items anyway, a list is probably the right call. Save dicts for when you're looking things up by name, ID, or property.

## Example (runnable)

```python
# List: ordered processing
<!-- more -->
temperatures = [20, 22, 21, 23, 25]
for i, temp in enumerate(temperatures):
    print(f"Day {i+1}: {temp}°C")

print("---")

# List: position-based access
<!-- more -->
scores = [85, 92, 78]
print(f"First score: {scores[0]}")

# Dict: lookup by identifier
<!-- more -->
students = {"Alice": 85, "Bob": 92, "Carol": 78}
print(f"Alice's score: {students['Alice']}")
```

**Expected output:**
```
Day 1: 20°C
Day 2: 22°C
Day 3: 21°C
Day 4: 23°C
Day 5: 25°C
---
First score: 85
Alice's score: 85
```

Notice how lists win when the question is "what's next?" but dicts win for "who scored 85?"

## Gotchas

* **Don't fake dict lookups with lists** — if you're writing `[x for x in list if x.id == target]`, stop. That's a sign you need a dict with IDs as keys.
* **Order matters in dicts too now** — Python 3.7+ dicts maintain insertion order, blurring the lines. But lists still signal "this is a sequence" more clearly.
* **JSON conversion** — lists become JSON arrays `[]`, dicts become objects `{}`. Match your data structure to your output format.

## See also

* [[When should you use a Python list?]](./when-to-use-python-list.md)
* [[Which is better — list or dictionary in Python?]](./which-is-better-list-or-dictionary.md)
* External: [https://docs.python.org/3/tutorial/datastructures.html](https://docs.python.org/3/tutorial/datastructures.html)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "In what situations are lists preferred over dictionaries?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Pick lists when position matters more than identity. You're processing items in order? List. Accessing by numeric index like give me the 5th item? List. You don't have natural keys for lookup? List. They're perfect for sequences (time-series, ordered steps, history), collecting loop results, and when all items are the same type. Lists are simpler and lighter when you don't need the key-value relationship. If you find yourself iterating through all items anyway, a list is probably the right call. Save dicts for when you're looking things up by name, ID, or property."
    }
  }]
}
</script>
