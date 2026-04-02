## What is Recursion?
Recursion is when a function calls itself to solve a smaller version of the same problem. Every recursive solution has two essential parts: a **base case** (when to stop) and a **recursive case** (how to break the problem down).

---

## The Two Rules of Recursion

**Rule 1 — Base Case:** Every recursive function MUST have a condition that stops the recursion. Without it, you get infinite calls and a stack overflow crash.

**Rule 2 — Recursive Case:** Each call must move closer to the base case. If the problem isn't getting smaller, you'll never reach the base case.

---

## Classic Examples

### 1. Factorial

```python
def factorial(n):
    if n == 0:          # base case
        return 1
    return n * factorial(n - 1)  # recursive case

factorial(5)  # → 120  (5 × 4 × 3 × 2 × 1)
```

### 2. Fibonacci

```python
def fib(n):
    if n <= 1:           # base cases: fib(0)=0, fib(1)=1
        return n
    return fib(n-1) + fib(n-2)  # recursive case

fib(6)  # → 8
```

### 3. Sum of a List

```python
def list_sum(lst):
    if not lst:          # base case: empty list
        return 0
    return lst[0] + list_sum(lst[1:])  # recursive case

list_sum([1, 2, 3, 4])  # → 10
```

### 4. Reverse a String

```python
def reverse(s):
    if len(s) == 0:      # base case
        return s
    return reverse(s[1:]) + s[0]  # recursive case

reverse("hello")  # → "olleh"
```

### 5. Binary Search (Recursive)

```python
def binary_search(arr, target, low, high):
    if low > high:       # base case: not found
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1)
```

---

## The Call Stack — What Happens in Memory---

## Types of Recursion---

## Recursion vs Iteration

| Feature | Recursion | Iteration |
|---|---|---|
| Code clarity | Often cleaner for tree/graph problems | Better for simple loops |
| Memory | Uses call stack (each frame) | Constant memory |
| Speed | Slightly slower (function call overhead) | Generally faster |
| Risk | Stack overflow if too deep | No stack risk |
| Best for | Trees, graphs, divide & conquer | Arrays, counters, simple loops |

---

## Memoization — Fixing Slow Recursion

Without memoization, `fib(6)` recomputes `fib(2)` multiple times. Memoization caches results so each subproblem is solved only once.

```python
# Without memoization — O(2^n), very slow
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)

# With memoization — O(n), fast
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)

# Manual memoization (same idea)
memo = {}
def fib(n):
    if n in memo: return memo[n]
    if n <= 1: return n
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]
```

---

## Tree Traversal — Recursion's Strongest Use Case

Recursion shines on tree structures because each node looks like the root of a smaller tree.

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Inorder  (Left → Root → Right)
def inorder(node):
    if node is None: return
    inorder(node.left)
    print(node.val)
    inorder(node.right)

# Preorder  (Root → Left → Right)
def preorder(node):
    if node is None: return
    print(node.val)
    preorder(node.left)
    preorder(node.right)

# Postorder  (Left → Right → Root)
def postorder(node):
    if node is None: return
    postorder(node.left)
    postorder(node.right)
    print(node.val)

# Height of a tree
def height(node):
    if node is None: return 0
    return 1 + max(height(node.left), height(node.right))
```

---

## Common Mistakes & Fixes---

## Complexity of Common Recursive Algorithms

| Algorithm | Time | Space (Stack) |
|---|---|---|
| Factorial | O(n) | O(n) |
| Fibonacci (naive) | O(2ⁿ) | O(n) |
| Fibonacci (memoized) | O(n) | O(n) |
| Binary Search | O(log n) | O(log n) |
| Merge Sort | O(n log n) | O(n) |
| Tree Traversal | O(n) | O(h) — h = height |
| Tower of Hanoi | O(2ⁿ) | O(n) |

---

## Quick Reference — How to Write Any Recursive Function

```
Step 1: Define the base case(s)
        → What is the simplest input? What does it return?

Step 2: Define the recursive case
        → How do I break this problem into a smaller version of itself?

Step 3: Ensure progress
        → Is each recursive call getting closer to the base case?

Step 4: Trust the recursion
        → Assume the function works correctly for smaller inputs.
          Just write what THIS call needs to do.
```

---

## When to Use Recursion

**Use recursion when:** the problem has a naturally recursive structure — trees, graphs, subsets, divide-and-conquer (merge sort, quicksort), backtracking (maze solving, N-queens), or hierarchical data.

**Prefer iteration when:** the problem is a simple loop, recursion depth would be large, or performance is critical (no overhead of function calls).