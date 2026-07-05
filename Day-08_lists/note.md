# Day 08 – Lists 🐍

## 📌 What is a List?

A **List** is an ordered and mutable collection used to store multiple values in a single variable.

Lists can store:

* Integers
* Floats
* Strings
* Booleans
* Mixed data types
* Even other lists

Lists are created using square brackets `[]`.

Example:

```python
fruits = ["Apple", "Banana", "Mango"]
```

---

# Why Use Lists?

Instead of creating multiple variables:

```python
student1 = "Ali"
student2 = "Ahmed"
student3 = "Arsalan"
```

We can use one list:

```python
students = ["Ali", "Ahmed", "Arsalan"]
```

Lists make programs shorter, cleaner, and easier to manage.

---

# Creating Lists

## List of Strings

```python
fruits = ["Apple", "Banana", "Mango"]
```

## List of Numbers

```python
numbers = [10, 20, 30, 40, 50]
```

## Mixed List

```python
data = ["Arsalan", 22, 75.5, True]
```

## Empty List

```python
marks = []
```

---

# List Indexing

Lists use **zero-based indexing**.

```text
Apple   Banana   Mango
  0        1        2
```

Negative Indexing:

```text
Apple   Banana   Mango
 -3       -2       -1
```

Example:

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits[0])
print(fruits[1])
print(fruits[-1])
```

Output:

```text
Apple
Banana
Mango
```

---

# List Slicing

Slicing extracts part of a list.

### Syntax

```python
list[start:end]
```

Example:

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
```

Output:

```text
[20, 30, 40]
```

More Examples:

```python
print(numbers[:3])
print(numbers[2:])
print(numbers[-3:])
```

---

# Changing List Items

Lists are **mutable**, meaning they can be modified.

```python
fruits = ["Apple", "Banana", "Mango"]

fruits[1] = "Orange"

print(fruits)
```

Output:

```text
['Apple', 'Orange', 'Mango']
```

---

# Adding Items

## append()

Adds an element to the end of the list.

```python
fruits.append("Grapes")
```

---

## insert()

Adds an element at a specific position.

```python
fruits.insert(1, "Orange")
```

---

## extend()

Adds all elements from another list.

```python
list1 = [1, 2, 3]
list2 = [4, 5]

list1.extend(list2)
```

Output:

```text
[1, 2, 3, 4, 5]
```

---

# Removing Items

## remove()

Removes an element by value.

```python
fruits.remove("Banana")
```

---

## pop()

Removes an element by index.

```python
fruits.pop()
```

Removes the last element.

```python
fruits.pop(1)
```

Removes the element at index 1.

---

## del

Deletes an element or the entire list.

```python
del fruits[0]
```

---

## clear()

Removes all elements.

```python
fruits.clear()
```

---

# List Length

Use the `len()` function.

```python
numbers = [10, 20, 30]

print(len(numbers))
```

Output:

```text
3
```

---

# Loop Through a List

Using a `for` loop:

```python
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)
```

---

Using Indexes:

```python
for i in range(len(fruits)):
    print(fruits[i])
```

---

# Membership Operators

Check whether an element exists.

```python
fruits = ["Apple", "Banana", "Mango"]

print("Apple" in fruits)
print("Orange" in fruits)
```

Output:

```text
True
False
```

---

# Useful List Methods

## sort()

Sorts the list in ascending order.

```python
numbers = [5, 2, 8, 1]

numbers.sort()

print(numbers)
```

Output:

```text
[1, 2, 5, 8]
```

---

## reverse()

Reverses the order.

```python
numbers.reverse()
```

---

## copy()

Creates a copy of a list.

```python
new_list = numbers.copy()
```

---

## count()

Counts occurrences.

```python
numbers = [1, 2, 2, 3, 2]

print(numbers.count(2))
```

Output:

```text
3
```

---

## index()

Returns the index of an element.

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits.index("Banana"))
```

Output:

```text
1
```

---

# Nested Lists

Lists can contain other lists.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])
```

Output:

```text
6
```

---

# Built-in Functions

```python
marks = [78, 85, 90, 67, 88]

print(max(marks))
print(min(marks))
print(sum(marks))
print(len(marks))
```

---

# Real-World Example

```python
subjects = ["Math", "Science", "English", "History", "Geography"]
marks = []

for subject in subjects:
    mark = int(input(f"Enter marks for {subject}: "))
    marks.append(mark)

highest = max(marks)
lowest = min(marks)
total = sum(marks)
average = total / len(marks)

print("\n----- Student Marks Report -----")

for subject, mark in zip(subjects, marks):
    print(f"{subject:<10}: {mark}")

print("-" * 30)
print(f"Highest Marks : {highest}")
print(f"Lowest Marks  : {lowest}")
print(f"Total Marks   : {total}")
print(f"Average Marks : {average:.2f}")
```

---

# Important Points

* Lists are **ordered**.
* Lists are **mutable** (can be modified).
* Lists allow duplicate values.
* Lists can store different data types.
* Indexing starts from `0`.
* Negative indexing starts from `-1`.

---

# Summary

In this lesson, you learned:

* Creating Lists
* Indexing
* Slicing
* Updating Elements
* Adding Items
* Removing Items
* Looping Through Lists
* Membership Operators
* List Methods
* Nested Lists
* Built-in Functions

Lists are one of the most important data structures in Python and are widely used in Data Engineering, Data Analysis, Machine Learning, and Web Development.

---

# Homework

* Create different types of lists.
* Practice indexing and slicing.
* Practice all list methods.
* Build a Student Marks Manager.
* Display subject-wise marks.
* Calculate highest, lowest, total, average, and grade.
* Push your work to GitHub.
