# Day 11 – Functions 🐍

## 📌 What is a Function?

A **function** is a reusable block of code that performs a specific task.

Instead of writing the same code multiple times, write it once inside a function and call it whenever needed.

Functions help make programs:

* Reusable
* Organized
* Easy to read
* Easy to maintain

---

# Why Use Functions?

Without Functions:

```python
print("Welcome to Python")
print("Welcome to Python")
print("Welcome to Python")
```

With Functions:

```python
def welcome():
    print("Welcome to Python")

welcome()
welcome()
welcome()
```

Output:

```text
Welcome to Python
Welcome to Python
Welcome to Python
```

---

# Defining a Function

### Syntax

```python
def function_name():
    # code
```

Example:

```python
def greet():
    print("Hello, Arsalan!")
```

---

# Calling a Function

A function executes only when it is called.

```python
def greet():
    print("Hello!")

greet()
```

Output:

```text
Hello!
```

---

# Functions with Parameters

Parameters allow a function to receive data.

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Arsalan")
greet("Ali")
```

Output:

```text
Hello, Arsalan!
Hello, Ali!
```

---

# Multiple Parameters

```python
def student(name, age):
    print(f"Name : {name}")
    print(f"Age  : {age}")

student("Arsalan", 22)
```

---

# Return Statement

A function can return a value back to the caller.

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

Output:

```text
30
```

---

# `print()` vs `return`

### Using `print()`

```python
def add(a, b):
    print(a + b)

result = add(10, 20)

print(result)
```

Output:

```text
30
None
```

Why?

Because `print()` displays the value but does **not** return it.

---

### Using `return`

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

Output:

```text
30
```

---

# Default Parameters

```python
def greet(name="Guest"):
    print(f"Hello, {name}")

greet()
greet("Arsalan")
```

Output:

```text
Hello, Guest
Hello, Arsalan
```

---

# Keyword Arguments

Arguments can be passed using parameter names.

```python
def student(name, age):
    print(name)
    print(age)

student(age=22, name="Arsalan")
```

Order does not matter when using keyword arguments.

---

# Variable-Length Arguments (`*args`)

Used when the number of arguments is unknown.

```python
def add(*numbers):
    return sum(numbers)

print(add(10, 20, 30))
```

Output:

```text
60
```

---

# Variable Scope

## Local Variable

A local variable exists only inside the function.

```python
def demo():
    x = 10
    print(x)

demo()
```

---

## Global Variable

A global variable can be accessed inside functions.

```python
x = 100

def demo():
    print(x)

demo()
```

Output:

```text
100
```

---

# Passing Data Between Functions

Instead of using global variables, functions should return values and accept parameters.

Example:

```python
def square(number):
    return number * number

result = square(5)

print(result)
```

Output:

```text
25
```

---

# Real-World Example

### Student Result System

```python
subjects = ["Math", "Science", "English"]
marks = {}

for subject in subjects:
    marks[subject] = int(input(f"{subject}: "))

def calculate_total(marks):
    return sum(marks.values())

total = calculate_total(marks)

print("Total:", total)
```

---

# Function Flow

```text
input_marks()
        │
        ▼
calculate_total()
        │
        ▼
calculate_average()
        │
        ▼
calculate_grade()
        │
        ▼
display_report()
```

Each function should perform **one specific task**.

---

# Built-in Functions

Python already provides many functions.

```python
numbers = [10, 20, 30]

print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
```

Output:

```text
3
30
10
60
```

---

# Important Points

* A function is created using `def`.
* A function runs only when called.
* Parameters receive data.
* Arguments are the values passed to parameters.
* `return` sends data back to the caller.
* `print()` only displays output.
* Functions make code reusable and organized.
* Each function should have one responsibility.

---

# Difference Between Parameter and Argument

| Parameter                       | Argument                            |
| ------------------------------- | ----------------------------------- |
| Variable in function definition | Actual value passed to the function |

Example:

```python
def greet(name):      # Parameter
    print(name)

greet("Arsalan")      # Argument
```

---

# Summary

In this lesson, you learned:

* Defining Functions
* Calling Functions
* Parameters
* Arguments
* Return Statement
* Default Parameters
* Keyword Arguments
* Variable-Length Arguments (`*args`)
* Variable Scope
* Passing Data Between Functions
* Function-Based Program Structure

Functions are one of the most important concepts in Python. Almost every real-world Python application uses functions to organize code into reusable, manageable blocks.

---

# Homework

* Create at least five functions.
* Practice functions with parameters.
* Practice functions that return values.
* Build a Student Result System using functions.
* Push your work to GitHub.
