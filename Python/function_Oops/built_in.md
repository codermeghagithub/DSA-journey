Here are the most commonly used and practically useful Python built-in functions, grouped by purpose:

---

## 🔢 Math & Numbers

| Function | What it does | Example |
|---|---|---|
| `abs(x)` | Absolute value | `abs(-5)` → `5` |
| `round(x, n)` | Round to n decimal places | `round(3.14159, 2)` → `3.14` |
| `pow(base, exp)` | Raise to a power | `pow(2, 10)` → `1024` |
| `divmod(a, b)` | Returns `(quotient, remainder)` | `divmod(10, 3)` → `(3, 1)` |
| `sum(iterable)` | Sum of all items | `sum([1,2,3])` → `6` |
| `max(iterable)` | Largest item | `max([3,1,4])` → `4` |
| `min(iterable)` | Smallest item | `min([3,1,4])` → `1` |

---

## 🔤 Type Conversion

| Function | What it does | Example |
|---|---|---|
| `int(x)` | Convert to integer | `int("42")` → `42` |
| `float(x)` | Convert to float | `float("3.14")` → `3.14` |
| `str(x)` | Convert to string | `str(100)` → `"100"` |
| `bool(x)` | Convert to boolean | `bool(0)` → `False` |
| `list(x)` | Convert to list | `list("abc")` → `['a','b','c']` |
| `tuple(x)` | Convert to tuple | `tuple([1,2])` → `(1, 2)` |
| `set(x)` | Convert to set (unique items) | `set([1,1,2])` → `{1, 2}` |
| `dict(...)` | Create a dictionary | `dict(a=1, b=2)` |

---

## 📋 Sequences & Iterables

| Function | What it does | Example |
|---|---|---|
| `len(x)` | Length of object | `len([1,2,3])` → `3` |
| `range(start, stop, step)` | Generate a number sequence | `range(0, 10, 2)` |
| `enumerate(iterable)` | Index + value pairs | `enumerate(['a','b'])` → `(0,'a'), (1,'b')` |
| `zip(a, b)` | Pair up iterables | `zip([1,2], ['a','b'])` → `(1,'a'), (2,'b')` |
| `sorted(iterable)` | Return sorted list | `sorted([3,1,2])` → `[1,2,3]` |
| `reversed(iterable)` | Return reversed iterator | `list(reversed([1,2,3]))` |
| `map(func, iterable)` | Apply function to each item | `map(str, [1,2,3])` |
| `filter(func, iterable)` | Keep items where func is True | `filter(lambda x: x>2, [1,2,3])` |

---

## 💬 Input / Output

| Function | What it does | Example |
|---|---|---|
| `print(*objects)` | Print to console | `print("Hello", "World")` |
| `input(prompt)` | Read user input | `name = input("Enter name: ")` |
| `open(file, mode)` | Open a file | `open("file.txt", "r")` |
| `format(value, spec)` | Format a value | `format(3.14159, ".2f")` → `"3.14"` |

---

## 🔍 Object Inspection

| Function | What it does | Example |
|---|---|---|
| `type(x)` | Get type of object | `type(42)` → `<class 'int'>` |
| `isinstance(x, type)` | Check if x is of a type | `isinstance(42, int)` → `True` |
| `dir(x)` | List attributes/methods | `dir([])` |
| `help(x)` | Show documentation | `help(str)` |
| `id(x)` | Unique identity (memory address) | `id(42)` |
| `hasattr(obj, name)` | Check if attribute exists | `hasattr([], 'append')` → `True` |
| `getattr(obj, name)` | Get attribute by name | `getattr([], '__len__')` |

---

## 🔢 Number Bases

| Function | What it does | Example |
|---|---|---|
| `bin(x)` | Integer → binary string | `bin(10)` → `'0b1010'` |
| `hex(x)` | Integer → hex string | `hex(255)` → `'0xff'` |
| `oct(x)` | Integer → octal string | `oct(8)` → `'0o10'` |
| `ord(char)` | Character → Unicode code point | `ord('A')` → `65` |
| `chr(code)` | Unicode code point → character | `chr(65)` → `'A'` |

---

## ✅ Logic Helpers

| Function | What it does | Example |
|---|---|---|
| `all(iterable)` | True if **all** items are truthy | `all([1, 2, 3])` → `True` |
| `any(iterable)` | True if **any** item is truthy | `any([0, 0, 1])` → `True` |
| `callable(x)` | Check if x can be called | `callable(print)` → `True` |

---

These ~35 functions cover the vast majority of everyday Python programming. The ones you'll reach for most often are `print`, `len`, `range`, `type`, `isinstance`, `enumerate`, `zip`, `sorted`, `map`, `filter`, `open`, `int`/`str`/`float`, `max`/`min`, and `sum`.