# Day 12 – Modules & Packages 📦🐍

## 📌 What is a Module?

A **module** is a Python file (`.py`) that contains variables, functions, classes, or other Python code that can be reused in other programs.

Instead of writing the same code repeatedly, we can create a module once and import it wherever needed.

Example:

```python
# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

The file `calculator.py` is a **module**.

---

# Why Do We Use Modules?

Modules help us:

* Reuse code
* Keep programs organized
* Reduce duplicate code
* Make debugging easier
* Improve teamwork on large projects

Instead of writing everything in one file, we can divide our program into multiple modules.

---

# Importing a Module

Use the `import` keyword to import a module.

### Syntax

```python
import module_name
```

Example:

```python
import math

print(math.sqrt(25))
```

Output:

```text
5.0
```

---

# Importing Specific Functions

If you only need certain functions, import them directly.

### Syntax

```python
from module_name import function_name
```

Example:

```python
from math import sqrt

print(sqrt(64))
```

Output:

```text
8.0
```

---

# Importing Multiple Functions

```python
from math import sqrt, factorial

print(sqrt(81))
print(factorial(5))
```

Output:

```text
9.0
120
```

---

# Importing with an Alias

An alias gives a shorter name to a module.

### Syntax

```python
import module_name as alias
```

Example:

```python
import math as m

print(m.pi)
print(m.sqrt(49))
```

Output:

```text
3.141592653589793
7.0
```

---

# The `math` Module

The `math` module provides mathematical functions and constants.

Example:

```python
import math

print(math.pi)
print(math.e)
print(math.sqrt(36))
print(math.pow(2, 5))
print(math.factorial(5))
print(math.ceil(3.2))
print(math.floor(3.8))
```

---

# The `random` Module

The `random` module is used to generate random values.

### Random Integer

```python
import random

print(random.randint(1, 100))
```

### Random Choice

```python
import random

fruits = ["Apple", "Banana", "Mango"]

print(random.choice(fruits))
```

### Shuffle a List

```python
import random

numbers = [1, 2, 3, 4, 5]

random.shuffle(numbers)

print(numbers)
```

---

# The `datetime` Module

Used for working with dates and time.

```python
from datetime import datetime

current = datetime.now()

print(current)
```

Current Date Only:

```python
from datetime import date

print(date.today())
```

---

# The `time` Module

Used for time-related operations.

```python
import time

print(time.time())
```

---

# The `os` Module

Used for interacting with the operating system.

Example:

```python
import os

print(os.getcwd())
```

Output:

```text
Displays the current working directory.
```

---

# The `sys` Module

Provides information about the Python interpreter.

Example:

```python
import sys

print(sys.version)
```

Output:

```text
Displays the installed Python version.
```

---

# Creating Your Own Module

### calculator.py

```python
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
```

### main.py

```python
import calculator

print(calculator.add(10, 20))
print(calculator.multiply(5, 6))
```

Output:

```text
30
30
```

---

# What is a Package?

A **package** is a folder that contains multiple related Python modules.

Example:

```text
school/
│
├── student.py
├── teacher.py
├── marks.py
└── __init__.py
```

Here, `school` is a package.

---

# Module vs Package

| Module                                 | Package                              |
| -------------------------------------- | ------------------------------------ |
| A single `.py` file                    | A folder containing multiple modules |
| Contains functions, variables, classes | Organizes related modules            |
| Imported using `import`                | Contains multiple importable modules |

---

# Project Structure Example

```text
Student_Result_System/
│
├── main.py
├── marks.py
├── grade.py
├── report.py
└── utils.py
```

Each file performs one specific task.

---

# Built-in Modules Covered

| Module     | Purpose                        |
| ---------- | ------------------------------ |
| `math`     | Mathematical operations        |
| `random`   | Random numbers and selections  |
| `datetime` | Date and time                  |
| `time`     | Time functions                 |
| `os`       | Operating system interaction   |
| `sys`      | Python interpreter information |

---

# Advantages of Modules

* Code Reusability
* Better Organization
* Easy Maintenance
* Faster Development
* Easier Testing
* Improved Readability
* Better Team Collaboration

---

# Important Points

* A module is a `.py` file.
* A package is a folder containing modules.
* Use `import` to include a module.
* Use `from module import function` to import specific functions.
* Use `as` to create an alias.
* Python provides many built-in modules.
* You can create your own custom modules.

---

# Summary

In this lesson, you learned:

* What a module is
* What a package is
* Importing modules
* Importing specific functions
* Using aliases
* Built-in modules (`math`, `random`, `datetime`, `time`, `os`, `sys`)
* Creating your own module
* Organizing Python projects using modules and packages

Modules are an essential part of Python programming. As your programs become larger, dividing them into multiple modules makes them cleaner, easier to maintain, and more reusable.

---

# Homework

1. Practice using the `math` module.
2. Generate random numbers using the `random` module.
3. Display the current date and time.
4. Create your own `calculator.py` module.
5. Complete the Calculator Challenge.
6. Push today's work to GitHub.

---

# Interview Questions

### 1. What is a module?

A module is a Python file that contains reusable code such as functions, variables, and classes.

---

### 2. What is a package?

A package is a folder containing multiple related Python modules.

---

### 3. What is the difference between `import math` and `from math import sqrt`?

* `import math` imports the entire module and functions are accessed using `math.function_name()`.
* `from math import sqrt` imports only the `sqrt()` function, so it can be used directly.

---

### 4. Why do we use modules?

To organize code, improve reusability, reduce duplication, and make programs easier to maintain.

---

## Git Commit

```bash
git add .
git commit -m "Day 12 - Modules & Packages Completed"
git push
```

---

# 🎯 Key Takeaway

> **A module is a reusable Python file. A package is a collection of related modules. By organizing code into modules and packages, you can build clean, scalable, and professional Python applications.**
