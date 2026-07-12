# Day 10 – Dictionaries 🐍

## 📌 What is a Dictionary?

A **dictionary** is an unordered collection of **key-value pairs**.

Unlike lists and tuples, dictionaries use **keys** instead of indexes to access data.

A dictionary is created using **curly braces `{}`**.

Example:

```python
student = {
    "name": "Arsalan",
    "age": 22,
    "city": "Latur"
}
```

Here:

* **Key** → `"name"`
* **Value** → `"Arsalan"`

---

# Why Use Dictionaries?

Dictionaries make data more meaningful.

Instead of:

```python
student = ["Arsalan", 22, "Latur"]
```

Use:

```python
student = {
    "name": "Arsalan",
    "age": 22,
    "city": "Latur"
}
```

This makes the program easier to read and maintain.

---

# Creating a Dictionary

```python
student = {
    "name": "Arsalan",
    "age": 22,
    "city": "Latur"
}

print(student)
```

Output:

```text
{'name': 'Arsalan', 'age': 22, 'city': 'Latur'}
```

---

# Accessing Values

## Using Square Brackets

```python
print(student["name"])
print(student["age"])
```

Output:

```text
Arsalan
22
```

---

## Using `get()`

```python
print(student.get("city"))
```

Output:

```text
Latur
```

### Why use `get()`?

If the key doesn't exist:

```python
print(student.get("salary"))
```

Output:

```text
None
```

But:

```python
print(student["salary"])
```

Raises:

```text
KeyError
```

So `get()` is safer.

---

# Adding New Items

```python
student["course"] = "Python"

print(student)
```

Output:

```text
{'name': 'Arsalan', 'age': 22, 'city': 'Latur', 'course': 'Python'}
```

---

# Updating Values

```python
student["city"] = "Pune"
```

Or:

```python
student.update({"city": "Pune"})
```

### Important

`update()` modifies the dictionary **in place** and returns **None**.

Wrong:

```python
print(student.update({"city": "Pune"}))
```

Output:

```text
None
```

Correct:

```python
student.update({"city": "Pune"})
print(student)
```

---

# Removing Items

## `pop()`

```python
student.pop("city")
```

Removes a key-value pair by key.

---

## `del`

```python
del student["age"]
```

Deletes a key-value pair.

---

## `clear()`

```python
student.clear()
```

Removes all items from the dictionary.

---

# Dictionary Length

```python
print(len(student))
```

Output:

```text
3
```

---

# Looping Through a Dictionary

## Keys

```python
for key in student:
    print(key)
```

Or:

```python
for key in student.keys():
    print(key)
```

---

## Values

```python
for value in student.values():
    print(value)
```

---

## Keys and Values

```python
for key, value in student.items():
    print(f"{key}: {value}")
```

Output:

```text
name: Arsalan
age: 22
city: Latur
```

---

# Dictionary Methods

## `keys()`

Returns all keys.

```python
print(student.keys())
```

---

## `values()`

Returns all values.

```python
print(student.values())
```

---

## `items()`

Returns key-value pairs.

```python
print(student.items())
```

---

## `update()`

Updates existing values or adds new ones.

```python
student.update({"course": "Big Data"})
```

---

## `copy()`

Creates a copy of the dictionary.

```python
new_student = student.copy()
```

---

# Nested Dictionaries

```python
students = {
    "student1": {
        "name": "Ali",
        "marks": 85
    },
    "student2": {
        "name": "Arsalan",
        "marks": 92
    }
}
```

Accessing data:

```python
print(students["student2"]["marks"])
```

Output:

```text
92
```

---

# Formatting Output

Use alignment inside f-strings.

```python
print(f"{'Name':<20}: Arsalan")
print(f"{'Course':<20}: Big Data")
```

Output:

```text
Name                : Arsalan
Course              : Big Data
```

`<20` means:

* `<` → Left align
* `20` → Reserve 20 spaces

---

# Real-World Example

```python
student = {
    "Name": "Arsalan",
    "Roll Number": 60,
    "Course": "Big Data",
    "Maths Marks": 95,
    "Science Marks": 90,
    "English Marks": 85
}

print("----------- Student Report Card ------------")

for key, value in student.items():
    print(f"{key:<20}: {value}")
```

---

# Calculating Total and Average

```python
count = 0
total = 0

for key, value in student.items():
    if "Marks" in key:
        total += value
        count += 1

average = total / count
```

This method automatically works even if more subjects are added.

---

# Assigning Grade

```python
grades = {
    90: "A",
    80: "B",
    70: "C",
    60: "D",
    0: "F"
}

for minimum_marks in grades:
    if average >= minimum_marks:
        grade = grades[minimum_marks]
        break
```

---

# Built-in Functions

```python
marks = {
    "Math": 95,
    "Science": 90,
    "English": 85
}

print(sum(marks.values()))
print(max(marks.values()))
print(min(marks.values()))
print(len(marks))
```

---

# Difference Between List and Dictionary

| List               | Dictionary            |
| ------------------ | --------------------- |
| Uses indexes       | Uses keys             |
| Ordered collection | Key-value collection  |
| Access by index    | Access by key         |
| Good for sequences | Good for labeled data |

---

# Important Points

* Dictionaries store **key-value pairs**.
* Keys must be **unique**.
* Values can be duplicated.
* Access data using keys.
* `get()` is safer than `[]` when the key may not exist.
* `update()` modifies the dictionary and returns `None`.
* `items()` is the best way to loop through keys and values together.

---

# Summary

In this lesson, you learned:

* Creating dictionaries
* Accessing values
* Adding items
* Updating values
* Removing items
* Dictionary methods
* Looping through dictionaries
* Nested dictionaries
* Formatting output
* Building a Student Report Card

Dictionaries are one of the most powerful data structures in Python and are heavily used in APIs, JSON, web development, data engineering, and machine learning.

---

# Homework

* Create your own dictionary.
* Practice all dictionary methods.
* Build a Student Report Card.
* Calculate total, average, and grade automatically.
* Push your work to GitHub.
