---
title: "How to Slice a List in Python?"
description: "Learn how to slice lists in Python using slice function and syntax with practical examples."
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: python, lists, indexing, slicing
---

# How to Slice a List in Python?

Slicing lets us extract or modify a subsequence of a list. In Python, we use the `[start:end:step]` syntax or the `slice()` function for this.

<div class="toc" markdown="1">
## Contents
- [Basic usage of slices](#basic-usage-of-slices)
    - [`start:stop`](#startstop)
    - [`start:stop:step`](#startstopstep)
    - [Error handling](#error-handling)
- [Working with negative indices](#working-with-negative-indices)
    - [Negative `start` and `stop` values](#negative-start-and-stop-values)
    - [Negative `step` value](#negative-step-value)
- [Creating reusable slice objects with `slice()`](#creating-reusable-slice-objects-with-slice)
    - [Using `slice()` with two arguments](#using-slice-with-two-arguments)
    - [Using `slice()` with one argument](#using-slice-with-one-argument)
    - [Creating an empty slice](#creating-an-empty-slice)

</div>



## Basic usage of slices

### `list[start:stop]`
In Python slicing, `[start:stop]` extracts elements from the `start` index up to, but not including, the `stop` index. The range follows the pattern `start <= x < stop`, where the element at `start` is included but the element at `stop` is excluded.

```python title="Example 1"
fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
print(fruits[2:5])  
>>> ["cherry", "date", "elderberry"]
```
In the Example 1, `fruits[2:5]` extracts `["cherry", "date", "elderberry"]` from the list. Notice that the element at index `2` is included and the element at index `5` is excluded.

#### Omitting the `start`  or `stop` index
If you leave out the `start` value, Python takes elements from the beginning. If you leave out the `stop` value, it goes to the end. Leaving out both gives you the whole sequence.

```python title="Example 2"
fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
print(fruits[:5])  
>>> ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits[5:])  
>>> ["fig", "grape"]
print(fruits[:])  
>>> ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
```

In the Example 2, `fruits[:5]` extracts `["apple", "banana", "cherry", "date", "elderberry"]` from the list, `fruits[5:]` extracts `["fig", "grape"]` from the list, and `fruits[:]` extracts the whole list.

### `list[start:stop:step]`

The step parameter sets how many elements you skip in a slice. Used with start and stop, it looks like this: `[start:stop:step]`. For example, step 2 picks every second element, and step 3 picks every third element and so on.

```python title="Example 3"
fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
print(fruits[::2])
>>> ["apple", "cherry", "elderberry", "grape"]
print(fruits[1::2])
>>> ["banana", "date", "fig"]
```

In the Example 3, `fruits[::2]` extracts `["apple", "cherry", "elderberry", "grape"]` from the list by skipping every second element. on the other hand, `fruits[1::2]` extracts `["banana", "date", "fig"]` from the list by skipping every second element starting from the second element.

### Error Handling
If you try to access an index that is out of range, Python will raise an `IndexError` exception. But if you use slicing, it will return an empty list instead of raising an error. This is useful because it allows you to handle out-of-range indices gracefully without crashing your program.

```python title="Example 4"
fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
print(fruits[100:200])
>>> []
```
Also, if the start index is greater than the stop index, Python will return an empty list without raising an error.

```python title="Example 5"
fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
print(fruits[5:2])
>>> []
```

## Working with negative indices
### Negative `start` and `stop` values
Negative indices count backward from the end of a sequence, with -1 representing the last element, -2 the second-to-last, and so on.

```python title="Example 6"
fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
print(fruits[-2:])
>>> ["fig", "grape"]
print(fruits[:-2])
>>> ["apple", "banana", "cherry", "date", "elderberry"]
```

In the Example 6, `fruits[-2:]` extracts `["fig", "grape"]` from the list by starting from the second last element and going to the end. On the other hand, `fruits[:-2]` extracts `["apple", "banana", "cherry", "date", "elderberry"]` from the list by starting from the beginning and going up to the second last element.

### Negative `step` value
Negative step values reverse the traversal direction, extracting elements from right to left.
When using a negative step, extraction begins at the start position. If start comes before stop in the sequence order, the result is an empty list.

```python title="Example 7"
fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
print(fruits[::-1])
>>> ["grape", "fig", "elderberry", "date", "cherry", "banana", "apple"]
```

In the Example 7, `fruits[::-1]` reverses the list by extracting elements from right to left.

When `step` is negative and you omit `start`, Python begins from the end. Omitting `stop` continues to the beginning. Omitting both traverses the entire sequence. Setting `step` to `-1` with both `start` and `stop` omitted creates a reversed copy of the sequence. Here is an example:

```python title="Example 8"
fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
print(fruits[::-1])
>>> ["grape", "fig", "elderberry", "date", "cherry", "banana", "apple"]
print(fruits[3::-1])
>>> ["date", "cherry", "banana", "apple"]
print(fruits[:-3:-1])
>>> ["fig", "elderberry", "date"]
```

In the Example 8, `fruits[::-1]` reverses the whole list by extracting elements from right to left.
On the other hand, `fruits[3::-1]` reverses the list by extracting elements from the third element to the beginning. Similarly, `fruits[:-3:-1]` reverses the list by extracting elements from the third last element to the end.


For reversing sequences, Python also provides the `reverse()` and `reversed()` methods, which offer alternative approaches depending on your needs.


## Creating reusable slice objects with `slice()`

Python's built-in `slice()` function creates slice objects that can be stored and reused. This is useful when you need to apply the same slice operation multiple times across different sequences.

The syntax `slice(start, stop, step)` is functionally equivalent to `[start:stop:step]`.

```python title="Example 9"
fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
sl = slice(2, 5, 2)
print(fruits[sl])
>>> ["cherry", "elderberry"]
```

In the Example 9, `slice(2, 5, 2)` creates a slice object that can be used to extract `["cherry", "elderberry"]` from the list.

### Using `slice()` with two arguments
When only two arguments are provided, `step` defaults to `None`, which behaves the same as `start:stop`.

```python title="Example 10"
sl = slice(2, 5)
print(sl)
>>> slice(2, 5, None)

print(l[sl])
>>> ["cherry", "elderberry"]
```

In the Example 10, `slice(2, 5)` creates a slice object that can be used to extract `["cherry", "elderberry"]` from the list.

### Using `slice()` with one argument
With a single argument, both `start` and `step` default to `None`, equivalent to `:stop`.

```python title="Example 11"
sl = slice(2)
print(sl)
>>> slice(None, 2, None)

print(l[sl])
>>> ["apple", "banana"]
```

In the Example 11, `slice(2)` creates a slice object that can be used to extract `["apple", "banana"]` from the list.
### Creating an empty slice

Calling `slice()` without arguments raises a `TypeError`. To create a slice equivalent to `:` (selecting all elements), explicitly pass `None` for all parameters.

```python title="Example 12"
sl = slice()
>>> TypeError: slice expected at least 1 arguments, got 0

sl = slice(None)
print(sl)
>>> slice(None, None, None)

print(fruits[sl])
>>> ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
```

## See also

* [How do you access elements in a Python list?](how-to-access-elements-in-list.md)
* [[What is [-1] in a Python list?]](what-is-negative-one-in-list.md)
* External: [https://docs.python.org/3/tutorial/introduction.html#lists](https://docs.python.org/3/tutorial/introduction.html#lists)

