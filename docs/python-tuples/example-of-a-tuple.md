---
title: "What is an example of a tuple?"
description: "Common examples: coordinates (x, y), RGB colors (255, 0, 0), database rows, function returns."
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: Subhajit Bhar, freelance data scientist, OCR, NLP, LLM, RAG, knowledge base, python, tuple, examples
  - name: Publisher
    content: Subhajit Bhar
date: 2025-10-07
updated: "2025-10-07"
---

# What is an example of a tuple?

<!-- more -->

!!! info "In short"
    Common tuple examples: coordinates `(x, y, z)`, RGB colors `(255, 128, 0)`, date/time values `(2025, 10, 7)`, function returns `(status, message)`, database rows `(id, name, email)`, constant configurations `(HOST, PORT, PROTOCOL)`. Any time you have related values that form a fixed structure, that's tuple territory. They're perfect for representing records, points in space, or grouped values that travel together. The pattern: if the number of elements is fixed and each position has meaning, use a tuple.

Here are real-world tuple examples you'll encounter:

```python
# 1. Coordinates (2D, 3D)
point_2d = (10, 20)
point_3d = (10, 20, 30)
x, y = point_2d

# 2. RGB/RGBA colors
red = (255, 0, 0)
semi_transparent_blue = (0, 0, 255, 128)

# 3. Date components
date = (2025, 10, 7)  # year, month, day
year, month, day = date

# 4. Function returns
def divide_with_remainder(a, b):
    return (a // b, a % b)

quotient, remainder = divide_with_remainder(17, 5)
print(f"17 ÷ 5 = {quotient} remainder {remainder}")

# 5. Database-style records
employee = ("E001", "Alice Johnson", 30, "Engineering")
emp_id, name, age, dept = employee

# 6. Configuration tuples
DATABASE = ("localhost", 5432, "myapp_db")
host, port, dbname = DATABASE

# 7. Geographic coordinates
location = (40.7128, -74.0060)  # NYC latitude, longitude

# 8. Version numbers
version = (2, 5, 1)  # major, minor, patch
```

Each example shows fixed-size, heterogeneous (or homogeneous) data where the structure has meaning.

Tuples shine when each position represents something specific.

## Gotchas

* **Don't overuse tuples** — if you have more than 5 elements, consider a class or `namedtuple` for clarity. `employee[3]` is less clear than `employee.dept`.
* **Tuples aren't always better** — for a list of coordinates, use a list of tuples: `[(10, 20), (30, 40)]`. The outer collection is dynamic, the inner structures are fixed.
* **Type hints help** — `Tuple[int, int]` (from `typing`) documents that a function returns exactly two ints.

## See also

* [What are the practical uses of tuples in Python?](practical-uses-of-tuples-in-python.md)
* [How do you write a tuple in Python?](how-to-write-a-tuple-in-python.md)
* External: [https://docs.python.org/3/library/collections.html#collections.namedtuple](https://docs.python.org/3/library/collections.html#collections.namedtuple)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "What is an example of a tuple?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Common tuple examples: coordinates (x, y, z), RGB colors (255, 128, 0), date/time values (2025, 10, 7), function returns (status, message), database rows (id, name, email), constant configurations (HOST, PORT, PROTOCOL). Any time you have related values that form a fixed structure, that's tuple territory."
    }
  }]
}
</script>
