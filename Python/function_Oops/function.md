## 1. What is a Function?

A function is a reusable block of code that performs a specific task. It runs only when called.

---

## 2. Defining a Function

```python
def function_name(parameters):
    """Docstring (optional)"""
    # body
    return value
```

```python
def greet():
    print("Hello, World!")

greet()  # Output: Hello, World!
```

---

## 3. Parameters & Arguments

### Positional Arguments
```python
def add(a, b):
    return a + b

add(3, 5)  # 8
```

### Default Arguments
```python
def greet(name, msg="Hello"):
    print(f"{msg}, {name}!")

greet("Alice")          # Hello, Alice!
greet("Bob", "Hi")      # Hi, Bob!
```

### Keyword Arguments
```python
def student(name, age):
    print(f"{name} is {age} years old")

student(age=20, name="Riya")  # order doesn't matter
```

### `*args` – Variable Positional Arguments
```python
def total(*nums):
    return sum(nums)

total(1, 2, 3, 4)  # 10
```

### `**kwargs` – Variable Keyword Arguments
```python
def info(**details):
    for k, v in details.items():
        print(f"{k}: {v}")

info(name="Arjun", city="Kolkata")
```

### Combining All
```python
def demo(a, b=10, *args, **kwargs):
    print(a, b, args, kwargs)

demo(1, 2, 3, 4, x=5, y=6)
# 1 2 (3, 4) {'x': 5, 'y': 6}
```

---

## 4. Return Statement

```python
def square(n):
    return n * n

result = square(4)  # 16
```

A function returns `None` by default if no `return` is used. You can return **multiple values** as a tuple:

```python
def min_max(lst):
    return min(lst), max(lst)

lo, hi = min_max([3, 1, 9, 2])  # 1, 9
```

---

## 5. Scope – LEGB Rule

| Scope | Meaning |
|-------|---------|
| **L** – Local | Inside the current function |
| **E** – Enclosing | Outer function (for nested functions) |
| **G** – Global | Module level |
| **B** – Built-in | Python's built-in names |

```python
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)   # local
    inner()
    print(x)       # enclosing

outer()
print(x)           # global
```

### `global` and `nonlocal`
```python
count = 0
def increment():
    global count
    count += 1

def outer():
    x = 10
    def inner():
        nonlocal x
        x += 1
    inner()
    print(x)  # 11
```

---

## 6. Lambda Functions

Anonymous, single-expression functions.

```python
square = lambda x: x ** 2
square(5)  # 25

# With sorted/map/filter
nums = [3, 1, 4, 1, 5]
sorted(nums, key=lambda x: -x)   # [5, 4, 3, 1, 1]
list(map(lambda x: x*2, nums))    # [6, 2, 8, 2, 10]
list(filter(lambda x: x>2, nums)) # [3, 4, 5]
```

---

## 7. Nested Functions

```python
def outer(msg):
    def inner():
        print(msg)   # accesses outer's variable
    inner()

outer("Hello from nested!")
```

---

## 8. Closures

A nested function that **remembers** the enclosing scope even after the outer function has finished.

```python
def multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = multiplier(2)
double(5)   # 10
double(9)   # 18
```

---

## 9. Decorators

A function that **wraps another function** to extend its behavior.

```python
def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()
# Before
# Hello!
# After
```

### Decorator with Arguments
```python
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper

@decorator
def add(a, b):
    return a + b
```

---

## 10. Recursion

A function calling **itself**.

```python
def factorial(n):
    if n == 0:       # base case
        return 1
    return n * factorial(n - 1)

factorial(5)  # 120
```

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

---

## 11. Higher-Order Functions

Functions that take or return other functions.

```python
def apply(func, value):
    return func(value)

apply(lambda x: x**2, 4)  # 16
```

Built-ins: `map()`, `filter()`, `sorted()`, `reduce()` (from `functools`)

```python
from functools import reduce
reduce(lambda a, b: a + b, [1, 2, 3, 4])  # 10
```

---

## 12. Type Hints (Python 3.5+)

```python
def add(a: int, b: int) -> int:
    return a + b

def greet(name: str) -> None:
    print(f"Hello, {name}")
```

---

## 13. Docstrings

```python
def divide(a, b):
    """
    Divides a by b.

    Args:
        a (float): Numerator
        b (float): Denominator

    Returns:
        float: Result of division
    """
    return a / b

help(divide)  # prints the docstring
```




## *args and **kwargs in Python – Full Notes

1. Why Do We Need Them?
Sometimes you don't know how many arguments will be passed to a function. That's where *args and **kwargs come in.
*args**kwargsStands forVariable ArgumentsVariable Keyword ArgumentsPasses asTupleDictionarySyntax*args**kwargsArgumentsPositionalKeyword (name=value)

2. *args – Variable Positional Arguments
Collects any number of positional arguments into a tuple.
pythondef greet(*args):
    for name in args:
        print(f"Hello, {name}!")

greet("Alice")                  # Hello, Alice!
greet("Alice", "Bob", "Riya")   # Hello, Alice! Hello, Bob! Hello, Riya!
Doing math with *args
pythondef total(*args):
    print(type(args))   # <class 'tuple'>
    return sum(args)

total(1, 2, 3)        # 6
total(10, 20, 30, 40) # 100
Looping and indexing
pythondef show(*args):
    for i, val in enumerate(args):
        print(f"arg[{i}] = {val}")

show("a", "b", "c")
### arg[0] = a
### arg[1] = b
### arg[2] = c

3. **kwargs – Variable Keyword Arguments
Collects any number of keyword arguments into a dictionary.
pythondef info(**kwargs):
    print(type(kwargs))  # <class 'dict'>
    for key, value in kwargs.items():
        print(f"{key} = {value}")

info(name="Arjun", city="Kolkata", age=21)
### name = Arjun
### city = Kolkata
### age = 21
Practical example
pythondef create_profile(**kwargs):
    print("--- Profile ---")
    for k, v in kwargs.items():
        print(f"{k.capitalize()}: {v}")

create_profile(name="Sneha", course="Python", year=2)
### --- Profile ---
### Name: Sneha
### Course: Python
### Year: 2

4. Using *args and **kwargs Together
pythondef demo(*args, **kwargs):
    print("args   →", args)
    print("kwargs →", kwargs)

demo(1, 2, 3, name="Alice", age=25)
### args   → (1, 2, 3)
### kwargs → {'name': 'Alice', 'age': 25}
```

---

## 5. Combining Normal + `*args` + `**kwargs`

### ⚠️ Order Rule (MUST follow this order):
```
def func(normal, *args, **kwargs)
pythondef student(school, *subjects, **details):
    print("School  :", school)
    print("Subjects:", subjects)
    print("Details :", details)

student("DPS", "Math", "Science", "English",
        roll=42, grade="A")
### School  : DPS
### Subjects: ('Math', 'Science', 'English')
### Details : {'roll': 42, 'grade': 'A'}

6. Unpacking with * and **
You can also unpack a list/tuple into *args and a dict into **kwargs when calling a function.
Unpacking a list with *
pythondef add(a, b, c):
    return a + b + c

nums = [1, 2, 3]
add(*nums)   # Same as add(1, 2, 3) → 6
Unpacking a dict with **
pythondef greet(name, city):
    print(f"{name} from {city}")

data = {"name": "Riya", "city": "Mumbai"}
greet(**data)   # Riya from Mumbai
Unpacking both together
pythondef func(a, b, c, x, y):
    print(a, b, c, x, y)

args   = (1, 2, 3)
kwargs = {"x": 10, "y": 20}

func(*args, **kwargs)  # 1 2 3 10 20


#### 💡 Remember: The names args and kwargs are just conventions — you can use *numbers or **options, but *args / **kwargs is the standard style everyone follows.

# Python Generators – Complete Notes

---

## 1. What is a Generator?

A generator is a **special function** that returns values **one at a time** (lazily) instead of all at once. It **pauses** after each value and **resumes** from where it left off.

> Normal function → returns all at once
> Generator → yields one value at a time

---

## 2. `yield` vs `return`

```python
# Normal function
def normal():
    return [1, 2, 3]   # returns full list

# Generator function
def gen():
    yield 1   # pauses here, sends 1
    yield 2   # resumes, sends 2
    yield 3   # resumes, sends 3
```

| | `return` | `yield` |
|---|---|---|
| Returns | Once | Multiple times |
| Memory | Stores all | One at a time |
| Type | Value | Generator object |
| Resumes | ❌ | ✅ |

---

## 3. Creating & Using a Generator

```python
def count_up(n):
    for i in range(1, n+1):
        yield i

gen = count_up(3)

print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
# next(gen) again → StopIteration error
```

### Using in a `for` loop (most common)
```python
for val in count_up(5):
    print(val)
# 1 2 3 4 5
```

---

## 4. How It Works Internally

```python
def demo():
    print("Step 1")
    yield 10
    print("Step 2")
    yield 20
    print("Step 3")

g = demo()
next(g)   # prints "Step 1", returns 10
next(g)   # prints "Step 2", returns 20
next(g)   # prints "Step 3", StopIteration
```

> Each `next()` call **resumes** from the last `yield`.

---

## 5. Generator Expression

Just like list comprehension but with `()` — **lazy evaluation**.

```python
# List comprehension — stores all in memory
squares_list = [x**2 for x in range(10)]

# Generator expression — generates one at a time
squares_gen = (x**2 for x in range(10))

print(next(squares_gen))  # 0
print(next(squares_gen))  # 1
```

---

## 6. `send()` – Sending Values into a Generator

You can **send a value back** into a generator using `.send()`.

```python
def accumulator():
    total = 0
    while True:
        value = yield total   # receives sent value
        total += value

g = accumulator()
next(g)        # must prime the generator first
g.send(10)     # total = 10
g.send(20)     # total = 30
g.send(5)      # total = 35
```

---

## 7. `throw()` and `close()`

```python
def gen():
    try:
        yield 1
        yield 2
    except ValueError:
        print("Error caught!")

g = gen()
next(g)              # 1
g.throw(ValueError)  # Error caught!

# close() — stops the generator
g = gen()
next(g)
g.close()   # generator is terminated
```

---

## 8. `yield from` – Delegating to Sub-Generator

```python
def inner():
    yield 1
    yield 2

def outer():
    yield from inner()   # delegates to inner
    yield 3

for v in outer():
    print(v)   # 1 2 3
```

---

## 9. Infinite Generators

Generators are perfect for **infinite sequences** since they don't store everything in memory.

```python
def infinite_counter(start=0):
    while True:
        yield start
        start += 1

gen = infinite_counter()
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 2
# ...goes on forever, use with break!
```

---

## 10. Memory Efficiency

```python
import sys

lst = [x**2 for x in range(10000)]  # List
gen = (x**2 for x in range(10000))  # Generator

print(sys.getsizeof(lst))  # ~85,000 bytes
print(sys.getsizeof(gen))  # ~120 bytes ✅
```

> Generators are ideal for **large data**, **file reading**, **streams**.

---

## 11. Real-World Use Cases

### Reading large files line by line
```python
def read_file(path):
    with open(path) as f:
        for line in f:
            yield line.strip()

for line in read_file("data.txt"):
    print(line)
```

### Pipeline of generators
```python
def numbers():
    yield from range(1, 6)

def squared(gen):
    for n in gen:
        yield n ** 2

def evens(gen):
    for n in gen:
        if n % 2 == 0:
            yield n

# Chain them
pipeline = evens(squared(numbers()))
for val in pipeline:
    print(val)  # 4, 16
```

---

> 💡 **Key Rule:** A function with **even one `yield`** becomes a generator function. Calling it returns a **generator object**, not a value.


## Quick Reference Summary

| Concept | Keyword/Syntax |
|---|---|
| Define function | `def name():` |
| Default param | `def f(x=10)` |
| Variable args | `*args`, `**kwargs` |
| Return value | `return` |
| Anonymous fn | `lambda x: expr` |
| Global variable | `global var` |
| Outer variable | `nonlocal var` |
| Decorator | `@decorator_name` |
| Recursive call | Function calls itself |
| Type hint | `def f(x: int) -> str` |


## 12. Quick Summary

| Feature | Detail |
|---|---|
| `yield` | Pauses and returns a value |
| `next()` | Resumes generator |
| `send(val)` | Sends value into generator |
| `close()` | Stops the generator |
| `throw(err)` | Raises error inside generator |
| `yield from` | Delegates to another generator |
| Generator expression | `(x for x in ...)` |
| Memory | Very efficient — one item at a time |
