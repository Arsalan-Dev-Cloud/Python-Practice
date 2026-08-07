# Day 14 – Exception Handling ⚠️🐍

## 📌 What is Exception Handling?

An **exception** is an error that occurs while a Python program is running.

The Error handeling is very useful thing

Exception handling allows us to handle these errors gracefully instead of allowing the entire program to crash.

Example without exception handling:

```python
number = int(input("Enter a number: "))
print(100 / number)
```

If the user enters:

```text
0
```

Python raises:

```text
ZeroDivisionError: division by zero
```

Exception handling allows us to display a meaningful message instead.

---

# Basic `try-except`

The basic structure is:

```python
try:
    # Code that might cause an error

except:
    # Code that handles the error
```

Example:

```python
try:
    number = int(input("Enter a number: "))
    print(100 / number)

except:
    print("Something went wrong!")
```

---

# Catching Specific Exceptions

Instead of using a general `except`, it is better to catch specific exceptions.

```python
try:
    number = int(input("Enter a number: "))
    print(100 / number)

except ValueError:
    print("Please enter numbers only.")

except ZeroDivisionError:
    print("You cannot divide by zero.")
```

This makes programs easier to understand and debug.

---

# Multiple Exceptions

A single `try` block can have multiple `except` blocks.

```python
try:
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print(result)

except ValueError:
    print("Invalid input!")

except ZeroDivisionError:
    print("Cannot divide by zero!")
```

Different errors can therefore be handled differently.

---

# `else`

The `else` block runs only when **no exception occurs**.

```python
try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid input!")

else:
    print("You entered:", number)
```

### Valid Input

```text
Enter a number: 50
You entered: 50
```

### Invalid Input

```text
Enter a number: hello
Invalid input!
```

The `else` block does not execute when an exception occurs.

---

# `finally`

The `finally` block **always executes**, whether an exception occurs or not.

```python
try:
    number = int(input("Enter a number: "))
    print(number)

except ValueError:
    print("Invalid number!")

finally:
    print("Program finished.")
```

Valid input:

```text
Enter a number: 50
50
Program finished.
```

Invalid input:

```text
Enter a number: hello
Invalid number!
Program finished.
```

---

# Complete Exception Flow

```text
              try
               │
        ┌──────┴──────┐
        │             │
      Error        No Error
        │             │
        ▼             ▼
     except          else
        │             │
        └──────┬──────┘
               ▼
            finally
               │
               ▼
              END
```

Remember:

```text
try      → Try risky code
except   → Handle an exception
else     → Runs when there is no exception
finally  → Always runs
```

---

# `ValueError`

A `ValueError` occurs when a function receives an inappropriate value.

Example:

```python
number = int("hello")
```

Python cannot convert `"hello"` into an integer.

Handle it:

```python
try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Please enter a valid number.")
```

---

# `ZeroDivisionError`

Occurs when a number is divided by zero.

```python
result = 100 / 0
```

Handle it:

```python
try:
    number = int(input("Enter number: "))
    result = 100 / number

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

# `FileNotFoundError`

Occurs when Python tries to open a file that does not exist.

```python
with open("Student.txt", "r") as file:
    print(file.read())
```

Handle it:

```python
try:
    with open("Student.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("Student.txt does not exist.")
```

This combines **File Handling and Exception Handling**.

---

# `IndexError`

Occurs when accessing an index that doesn't exist.

```python
numbers = [10, 20, 30]

print(numbers[5])
```

Handle it:

```python
try:
    numbers = [10, 20, 30]

    print(numbers[5])

except IndexError:
    print("Index does not exist.")
```

---

# `KeyError`

Occurs when accessing a dictionary key that doesn't exist.

```python
student = {
    "Name": "Arsalan",
    "Marks": 90
}

print(student["Course"])
```

Handle it:

```python
try:
    print(student["Course"])

except KeyError:
    print("Key does not exist.")
```

---

# `TypeError`

Occurs when an operation is performed with incompatible data types.

Example:

```python
result = "10" + 20
```

Handle it:

```python
try:
    result = "10" + 20

except TypeError:
    print("Invalid data types.")
```

---

# `NameError`

Occurs when using a variable that has not been defined.

Example:

```python
print(student_name)
```

If `student_name` doesn't exist, Python raises `NameError`.

---

# Common Exceptions

| Exception           | Meaning                             |
| ------------------- | ----------------------------------- |
| `ValueError`        | Invalid value or conversion         |
| `TypeError`         | Wrong/incompatible data type        |
| `ZeroDivisionError` | Division by zero                    |
| `FileNotFoundError` | File doesn't exist                  |
| `KeyError`          | Dictionary key doesn't exist        |
| `IndexError`        | List/tuple index doesn't exist      |
| `NameError`         | Variable doesn't exist              |
| `OSError`           | Operating-system/file-related error |

You do not need to memorize every Python exception. Learn the common ones and become familiar with others as you encounter them.

---

# Getting the Actual Error Message

The exception can be stored in a variable.

```python
try:
    number = int(input("Enter number: "))
    result = 100 / number

except Exception as error:
    print("Error:", error)
```

Example:

```text
Enter number: 0

Error: division by zero
```

A commonly seen shorter version is:

```python
except Exception as e:
    print(e)
```

---

# Specific vs General Exceptions

General:

```python
except Exception as error:
```

can catch many types of exceptions.

However, when you know which errors are expected, prefer specific exceptions:

```python
except ValueError:
```

or:

```python
except ZeroDivisionError:
```

This makes the program's error handling clearer.

---

# `raise`

The `raise` keyword allows us to deliberately create an exception.

Example:

```python
age = int(input("Enter age: "))

if age < 0:
    raise ValueError("Age cannot be negative.")
```

Input:

```text
-5
```

produces a `ValueError`.

---

# Validating Marks with `raise`

```python
try:
    marks = int(input("Enter marks: "))

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")

    print("Marks:", marks)

except ValueError as error:
    print("Error:", error)
```

Now both of these are invalid:

```text
-10
150
```

while:

```text
90
```

is accepted.

---

# Why Use `raise`?

Sometimes Python itself doesn't consider something an error.

For example:

```python
marks = 150
```

is a perfectly valid integer to Python.

But according to our program's rules, marks should only be:

```text
0 – 100
```

Therefore, **we create our own exception**:

```python
if marks < 0 or marks > 100:
    raise ValueError("Marks must be between 0 and 100.")
```

This is called **validation**.

---

# Exception Handling with File Handling

Day 13 and Day 14 can be combined.

```python
try:
    with open("Student.txt", "r") as file:
        data = file.read()

except FileNotFoundError:
    print("Student file not found.")

else:
    print(data)

finally:
    print("File operation completed.")
```

---

# Day 14 Challenge – Student Record System

The challenge combines:

* User Input
* Dictionaries
* Loops
* File Handling
* Exception Handling
* Validation

Example:

```python
try:
    name = input("Enter Name     : ")
    roll_no = int(input("Enter Roll No. : "))
    course = input("Enter Course   : ")
    marks = int(input("Enter Marks    : "))

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")

    student = {
        "Name": name,
        "Roll No.": roll_no,
        "Course": course,
        "Marks": marks
    }

    with open("Student.txt", "a") as file:

        for key, value in student.items():
            file.write(f"{key:<10}: {value}\n")

        file.write("\n")

except ValueError as error:
    print(f"\nInvalid Input: {error}")

except OSError as error:
    print(f"\nFile Error: {error}")

else:
    print("\nStudent record saved successfully!")

finally:
    print("Program finished.")
```

---

# Challenge Program Flow

```text
User Input
    │
    ▼
   try
    │
    ├──── Invalid number ─────→ ValueError
    │
    ├──── Invalid marks ──────→ raise ValueError
    │
    ├──── File problem ───────→ OSError
    │
    ▼
Save Student.txt
    │
    ▼
   else
    │
    ▼
Success Message
    │
    ▼
 finally
    │
    ▼
Program Finished
```

---

# Difference Between Syntax Error and Exception

### Syntax Error

The Python code itself is written incorrectly.

```python
if age > 18
    print("Adult")
```

The missing `:` causes a syntax error.

### Exception

The program's syntax is correct, but something goes wrong while it runs.

```python
number = 10 / 0
```

This produces:

```text
ZeroDivisionError
```

Exception handling is mainly used for **runtime errors**, not for fixing invalid Python syntax.

---

# Important Points

* Exceptions occur while a program is running.
* `try` contains code that may fail.
* `except` handles an exception.
* Multiple `except` blocks can handle different errors.
* `else` runs when no exception occurs.
* `finally` always runs.
* `raise` manually creates an exception.
* Specific exceptions are usually better than a general `except`.
* Exception handling prevents expected runtime problems from crashing the program unexpectedly.
* Validation and exception handling are commonly used together.

---

# Real-World Uses

Exception handling is heavily used in:

### Web Development

```text
Invalid login
Invalid form data
API failure
Database connection failure
Missing records
File upload errors
```

### Data Engineering

```text
Missing files
Invalid CSV data
Database failures
API errors
Incorrect data types
Pipeline failures
```

So exception handling is an important professional Python skill.

---

# Summary

In Day 14, you learned:

* Exceptions
* `try`
* `except`
* Multiple exceptions
* `else`
* `finally`
* `raise`
* `ValueError`
* `ZeroDivisionError`
* `FileNotFoundError`
* `IndexError`
* `KeyError`
* `TypeError`
* `NameError`
* `OSError`
* Exception messages
* Input validation
* Exception handling with files

---

# Quick Revision

```python
try:
    # risky code

except ValueError:
    # handle ValueError

except ZeroDivisionError:
    # handle division by zero

else:
    # runs if no exception

finally:
    # always runs
```

And:

```python
raise ValueError("Custom error message")
```

---

# Git Commit

After completing Day 14:

```bash
git add .
git commit -m "Day 14 - Exception Handling Completed"
git push
```

---

# 🎯 Key Takeaway

> **`try` attempts the operation, `except` handles errors, `else` handles success, `finally` always executes, and `raise` lets us reject invalid data ourselves.**
