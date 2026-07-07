# Day 09 – Tuples 🐍

## 📌 What is a Tuple?

A **tuple** is an **ordered** and **immutable** collection of items.

* **Ordered** → Elements maintain their insertion order.
* **Immutable** → Elements cannot be changed after the tuple is created.
* Tuples can store different data types.
* Duplicate values are allowed.

Tuples are created using **parentheses `()`**.

Example:

```python id="g8j5yj"
fruits = ("Apple", "Banana", "Mango")
```

---

# Why Use Tuples?

Use tuples when the data should **not change**.

Examples:

* Days of the week
* Months of the year
* GPS Coordinates
* RGB Color Values
* Employee Records
* Database Query Results

Since tuples are immutable, they help protect data from accidental modification.

---

# Creating Tuples

## String Tuple

```python id="2qz6fr"
fruits = ("Apple", "Banana", "Mango")
```

---

## Integer Tuple

```python id="91t3hf"
numbers = (10, 20, 30, 40, 50)
```

---

## Mixed Tuple

```python id="03jlwm"
student = ("Arsalan", 22, True, 85.5)
```

---

## Empty Tuple

```python id="uzjvzr"
empty = ()
```

---

# Single-Element Tuple

⚠️ This is one of the most common beginner mistakes.

Wrong:

```python id="ckjlwm"
number = (10)
```

Output:

```python id="0ax3mr"
<class 'int'>
```

Correct:

```python id="e2tqgz"
number = (10,)
```

Output:

```python id="pbgmrv"
<class 'tuple'>
```

The comma (`,`) makes it a tuple.

---

# Tuple Indexing

Tuples use **zero-based indexing**.

```text id="8gnvgq"
Apple   Banana   Mango
  0        1        2
```

Negative Indexing:

```text id="w25ecv"
Apple   Banana   Mango
 -3       -2       -1
```

Example:

```python id="fjlwmq"
fruits = ("Apple", "Banana", "Mango")

print(fruits[0])
print(fruits[1])
print(fruits[-1])
```

Output:

```text id="v8my0m"
Apple
Banana
Mango
```

---

# Tuple Slicing

Slicing extracts part of a tuple.

### Syntax

```python id="hjlwm4"
tuple[start:end]
```

Example:

```python id="jjlwm5"
numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])
```

Output:

```text id="ljlwm6"
(20, 30, 40)
```

More Examples:

```python id="mjlwm7"
print(numbers[:3])
print(numbers[2:])
print(numbers[-3:])
```

---

# Tuple Length

Use the `len()` function.

```python id="njlwm8"
numbers = (10, 20, 30)

print(len(numbers))
```

Output:

```text id="ojlwm9"
3
```

---

# Loop Through a Tuple

```python id="pjlwm0"
fruits = ("Apple", "Banana", "Mango")

for fruit in fruits:
    print(fruit)
```

Output:

```text id="qjlwm1"
Apple
Banana
Mango
```

---

# Membership Operators

Check whether an item exists.

```python id="rjlwm2"
fruits = ("Apple", "Banana", "Mango")

print("Apple" in fruits)
print("Orange" in fruits)
```

Output:

```text id="sjlwm3"
True
False
```

---

# Tuple Methods

Tuples have only **two built-in methods**.

## `count()`

Counts the number of occurrences.

```python id="tjlwm4"
numbers = (1, 2, 2, 3, 2)

print(numbers.count(2))
```

Output:

```text id="ujlwm5"
3
```

---

## `index()`

Returns the index of the first occurrence.

```python id="vjlwm6"
fruits = ("Apple", "Banana", "Mango")

print(fruits.index("Banana"))
```

Output:

```text id="wjlwm7"
1
```

---

# Tuple Packing

Packing means storing multiple values into a single tuple.

```python id="xjlwm8"
employee = (101, "Arsalan", "Data Engineer", 60000, "Latur")
```

---

# Tuple Unpacking

Unpacking means assigning tuple values to individual variables.

```python id="yjlwm9"
employee = (101, "Arsalan", "Data Engineer", 60000, "Latur")

emp_id, name, department, salary, city = employee

print(emp_id)
print(name)
print(department)
print(salary)
print(city)
```

Output:

```text id="zjlwm0"
101
Arsalan
Data Engineer
60000
Latur
```

---

# Nested Tuples

A tuple can contain other tuples.

```python id="aa1bb2"
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print(matrix[1][2])
```

Output:

```text id="cc3dd4"
6
```

---

# Built-in Functions

```python id="ee5ff6"
marks = (80, 75, 90, 88, 70)

print(max(marks))
print(min(marks))
print(sum(marks))
print(len(marks))
```

Output:

```text id="gg7hh8"
90
70
403
5
```

---

# Difference Between List and Tuple

| List                  | Tuple                        |
| --------------------- | ---------------------------- |
| `[]`                  | `()`                         |
| Mutable               | Immutable                    |
| Can add/remove items  | Cannot add/remove items      |
| Many built-in methods | Only `count()` and `index()` |
| Slightly slower       | Slightly faster              |
| Uses more memory      | Uses less memory             |

---

# Real-World Example

```python id="ii9jj0"
employee_info = (1, "Arsalan", "Data Engineer", 60000, "Latur")

emp_id, name, department, salary, city = employee_info

print("----- Employee Information -----")
print(f"ID         : {emp_id}")
print(f"Name       : {name}")
print(f"Department : {department}")
print(f"Salary     : ₹{salary:,}")
print(f"City       : {city}")
```

Output:

```text id="kk1ll2"
----- Employee Information -----
ID         : 1
Name       : Arsalan
Department : Data Engineer
Salary     : ₹60,000
City       : Latur
```

---

# Important Points

* Tuples are ordered.
* Tuples are immutable.
* Tuples allow duplicate values.
* Tuples can store different data types.
* Indexing starts from `0`.
* Negative indexing starts from `-1`.
* A single-element tuple must include a comma.
* Use tuples for data that should remain unchanged.

---

# Summary

In this lesson, you learned:

* Creating Tuples
* Tuple Indexing
* Tuple Slicing
* Tuple Length
* Looping Through Tuples
* Membership Operators
* Tuple Methods
* Tuple Packing
* Tuple Unpacking
* Nested Tuples
* Built-in Functions
* Difference Between Lists and Tuples

Tuples are widely used in Python for storing fixed collections of data and are commonly returned by functions, database queries, and APIs.

---

# Homework

* Create different types of tuples.
* Practice indexing and slicing.
* Practice `count()` and `index()`.
* Create programs using tuple packing and unpacking.
* Build the Employee Information System.
* Push your work to GitHub.
