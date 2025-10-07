---
title: "When to use a list comprehension in Python?"
description: "Learn when list comprehensions improve code: readability, performance benefits, and when to stick with regular loops."
tags:
  - python
  - lists
  - comprehension
date: 2025-10-07
updated: "2025-10-07"
---

# When to use a list comprehension in Python?
<!-- more -->

!!! info "In short"
    Use comprehensions for simple, one-line transformations and filtering. They're faster than loops with `.append()` and more Pythonic. Perfect for mapping (`[x*2 for x in nums]`), filtering (`[x for x in nums if x > 0]`), or both together. But here's the rule: if it doesn't fit comfortably on one line or needs a comment to explain, use a regular loop. Nested comprehensions beyond two levels get unreadable fast. Comprehensions are about clarity and conciseness—when they hurt readability, you've gone too far.

## Example (runnable)

```python
# Good: simple transformation
<!-- more -->
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)

# Good: filtering
<!-- more -->
evens = [x for x in numbers if x % 2 == 0]
print(evens)

# Good: both
<!-- more -->
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(even_squares)

# Bad: too complex (don't do this)
<!-- more -->
# result = [f(x) if x > 0 else g(x) if x < 0 else h(x) 
#           for x in data if validate(x) and check(x)]
<!-- more -->
```

**Expected output:**
```
[1, 4, 9, 16, 25]
[2, 4]
[4, 16]
```

That last commented example? If you're tempted to write that, step back and use a loop.

## Gotchas

* **Readability beats cleverness** — if you need to think hard to understand your own comprehension, it's too complex. Break it down.
* **Memory with large datasets** — comprehensions build the entire list in memory. For millions of items, use generator expressions: `(x**2 for x in huge_range)`.
* **Side effects are confusing** — don't call functions with side effects in comprehensions like `[print(x) for x in items]`. It works but reads weird. Use a regular loop.

## See also

* [[How do you create lists using list comprehension?]](./create-lists-using-list-comprehension.md)
* [[How do you iterate over a list in Python?]](./how-to-iterate-over-a-list.md)
* External: [https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "When to use a list comprehension in Python?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Use comprehensions for simple, one-line transformations and filtering. They're faster than loops with .append() and more Pythonic. Perfect for mapping ([x*2 for x in nums]), filtering ([x for x in nums if x > 0]), or both together. But here's the rule: if it doesn't fit comfortably on one line or needs a comment to explain, use a regular loop. Nested comprehensions beyond two levels get unreadable fast. Comprehensions are about clarity and conciseness—when they hurt readability, you've gone too far."
    }
  }]
}
</script>
