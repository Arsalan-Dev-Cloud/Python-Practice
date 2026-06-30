# Day 02 – Data Types 🐍

## 📌 What is a Data Type?

A **data type** defines the kind of value stored in a variable. Python automatically identifies the data type based on the assigned value.

Example:

```python
name = "Arsalan"
age = 22
height = 5.8
is_student = True
```

---

# Basic Data Types in Python

## 1. Integer (`int`)

Stores whole numbers (positive, negative, or zero).

```python
age = 22
marks = 95
temperature = -10
```

Example Output:

```
22
```

---

## 2. Float (`float`)

Stores decimal numbers.

```python
height = 5.8
price = 199.99
```

Example Output:

```
5.8
```

---

## 3. String (`str`)

Stores text enclosed in single or double quotes.

```python
name = "Arsalan"
city = 'Latur'
```

Example Output:

```
Arsalan
```

---

## 4. Boolean (`bool`)

Represents one of two values:

* `True`
* `False`

```python
is_student = True
is_admin = False
```

---

# Checking the Data Type

Use the `type()` function to check the data type of a variable.

```python
name = "Arsalan"
age = 22
height = 5.8
student = True

print(type(name))
print(type(age))
print(type(height))
print(type(student))
```

Output:

```
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

---

# The `input()` Function

The `input()` function always returns a **string**.

```python
age = input("Enter your age: ")

print(age)
print(type(age))
```

If the user enters:

```
22
```

Output:

```
22
<class 'str'>
```

---

# Type Conversion (Casting)

Type conversion changes one data type into another.

## String to Integer

```python
age = int(input("Enter your age: "))
```

---

## String to Float

```python
height = float(input("Enter your height: "))
```

---

## Integer to String

```python
age = 22
text = str(age)

print(text)
```

---

## Float to Integer

```python
price = 199.99
whole = int(price)

print(whole)
```

Output:

```
199
```

> **Note:** Converting a float to an integer removes the decimal part instead of rounding.

---

# Practical Example

```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
```

---

# Important Points

* Python is a dynamically typed language.
* Variable types are assigned automatically.
* `input()` always returns a string.
* Use `int()`, `float()`, `str()`, and `bool()` for type conversion.
* Use `type()` to check the data type of any variable.

---

# Common Type Conversion Functions

| Function  | Purpose            | Example            |
| --------- | ------------------ | ------------------ |
| `int()`   | Convert to Integer | `int("25")`        |
| `float()` | Convert to Float   | `float("5.8")`     |
| `str()`   | Convert to String  | `str(22)`          |
| `bool()`  | Convert to Boolean | `bool(1)` → `True` |

---

# Summary

* Python has several built-in data types.
* The four fundamental data types are:

  * Integer (`int`)
  * Float (`float`)
  * String (`str`)
  * Boolean (`bool`)
* `type()` is used to identify the data type.
* `input()` always returns a string.
* Type conversion (casting) allows values to be converted between compatible data types.

---

# Homework

* Create variables of each basic data type.
* Print their values and data types.
* Take user input and convert it to `int` and `float`.
* Create a simple Student Profile program using different data types.
