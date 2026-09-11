# Big-O Complexity

## What is Big-O?

Big-O notation describes how the performance of an algorithm changes as the input size increases.

We usually use `n` to represent the size of the input.

For example:

```python
numbers = [10, 20, 30, 40, 50]
```

Here:

```text
n = 5
```

---

# Time Complexity

Time complexity tells us how the amount of work performed by an algorithm grows as the input gets larger.

## O(1) — Constant Time

The amount of work stays approximately the same regardless of the input size.

Example:

```python
def get_first(numbers):
    return numbers[0]
```

We directly access one element.

**Time Complexity: O(1)**

---

## O(log n) — Logarithmic Time

The problem gets significantly smaller at each step.

A common example is Binary Search.

For example, instead of checking every element, we repeatedly divide the search area in half.

**Time Complexity: O(log n)**

---

## O(n) — Linear Time

The amount of work grows directly with the input size.

Example:

```python
def print_all(numbers):
    for number in numbers:
        print(number)
```

If there are `n` elements, we process all `n` elements.

**Time Complexity: O(n)**

---

## O(n log n) — Linearithmic Time

This commonly appears in efficient sorting algorithms such as Merge Sort.

It is slower than O(n), but much better than O(n²) for large inputs.

**Time Complexity: O(n log n)**

---

## O(n²) — Quadratic Time

This commonly happens when we have a loop inside another loop.

Example:

```python
def print_pairs(numbers):
    for i in numbers:
        for j in numbers:
            print(i, j)
```

If there are `n` elements, we perform approximately `n × n` operations.

**Time Complexity: O(n²)**

---

# Space Complexity

Space complexity describes how much additional memory an algorithm needs as the input size increases.

## O(1) — Constant Space

The algorithm uses a fixed amount of extra memory.

Example:

```python
def add_numbers(a, b):
    result = a + b
    return result
```

The amount of extra memory doesn't grow with `n`.

**Space Complexity: O(1)**

---

## O(n) — Linear Space

The amount of extra memory grows with the input size.

Example:

```python
def copy_numbers(numbers):
    result = []

    for number in numbers:
        result.append(number)

    return result
```

If there are `n` elements, the new list can contain `n` elements.

**Space Complexity: O(n)**

---

# Common Complexities

| Big-O      | Name         | Example                 |
| ---------- | ------------ | ----------------------- |
| O(1)       | Constant     | Array access            |
| O(log n)   | Logarithmic  | Binary Search           |
| O(n)       | Linear       | Single loop             |
| O(n log n) | Linearithmic | Merge Sort              |
| O(n²)      | Quadratic    | Nested loops            |
| O(2ⁿ)      | Exponential  | Some recursive problems |

---

# How I Analyze Code

When looking at an algorithm, I ask:

### Time

> How many times does the code execute as `n` grows?

### Space

> How much additional memory does the code create as `n` grows?

---

# What I Learned

* Big-O describes how an algorithm scales.
* `O(1)` means constant work.
* `O(log n)` means the problem is repeatedly reduced.
* `O(n)` means work grows linearly.
* `O(n²)` often comes from nested loops.
* Space complexity measures additional memory usage.
* A good solution considers both time and space.
