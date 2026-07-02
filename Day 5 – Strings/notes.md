# Day 05 – Strings 🐍

## 📌 What is a String?

A **string** is a sequence of characters enclosed in single quotes (`' '`), double quotes (`" "`), or triple quotes (`''' '''` or `""" """`).

Strings are used to store text such as names, emails, addresses, passwords, and messages.

Example:

```python
name = "Arsalan"
city = 'Latur'
message = """Welcome to Python"""
```

---

# Creating Strings

```python
first_name = "Arsalan"
last_name = "Shaikh"

print(first_name)
print(last_name)
```

Output:

```
Arsalan
Shaikh
```

---

# String Indexing

Each character in a string has an index.

Example:

```
Python
012345
```

Negative indexing:

```
Python
-6 -5 -4 -3 -2 -1
```

Example:

```python
language = "Python"

print(language[0])
print(language[1])
print(language[-1])
```

Output:

```
P
y
n
```

---

# String Slicing

Slicing is used to extract a portion of a string.

Syntax:

```python
string[start:end]
```

Example:

```python
text = "DataEngineering"

print(text[0:4])
print(text[4:15])
print(text[:4])
print(text[4:])
print(text[-5:])
```

Output:

```
Data
Engineering
Data
Engineering
ering
```

---

# Length of a String

Use the `len()` function to count the number of characters.

```python
name = "Arsalan"

print(len(name))
```

Output:

```
7
```

---

# String Concatenation

Concatenation means joining two or more strings using the `+` operator.

```python
first = "Arsalan"
last = "Shaikh"

full_name = first + " " + last

print(full_name)
```

Output:

```
Arsalan Shaikh
```

---

# String Repetition

Use the `*` operator to repeat a string.

```python
print("Python " * 3)
```

Output:

```
Python Python Python
```

---

# Membership Operators

Membership operators check whether a character or substring exists in a string.

```python
name = "Arsalan"

print("A" in name)
print("z" in name)
print("x" not in name)
```

Output:

```
True
False
True
```

---

# Common String Methods

## `upper()`

Converts all characters to uppercase.

```python
name = "arsalan"

print(name.upper())
```

Output:

```
ARSALAN
```

---

## `lower()`

Converts all characters to lowercase.

```python
name = "ARSALAN"

print(name.lower())
```

Output:

```
arsalan
```

---

## `title()`

Converts the first letter of each word to uppercase.

```python
name = "shaikh arsalan"

print(name.title())
```

Output:

```
Shaikh Arsalan
```

---

## `capitalize()`

Capitalizes only the first letter of the first word.

```python
text = "python programming"

print(text.capitalize())
```

Output:

```
Python programming
```

---

## `strip()`

Removes spaces from the beginning and end of a string.

```python
text = "   Python   "

print(text.strip())
```

Output:

```
Python
```

---

## `replace()`

Replaces one substring with another.

```python
text = "I like Java"

print(text.replace("Java", "Python"))
```

Output:

```
I like Python
```

---

## `find()`

Returns the index of the first occurrence of a substring.

```python
text = "Python Programming"

print(text.find("Programming"))
```

Output:

```
7
```

If the substring is not found, it returns `-1`.

---

## `index()`

Works like `find()`, but raises an error if the substring is not found.

```python
text = "Python"

print(text.index("thon"))
```

---

## `count()`

Counts the number of occurrences of a character or substring.

```python
text = "banana"

print(text.count("a"))
```

Output:

```
3
```

---

## `startswith()`

Checks whether a string starts with a specific value.

```python
text = "Python"

print(text.startswith("Py"))
```

Output:

```
True
```

---

## `endswith()`

Checks whether a string ends with a specific value.

```python
file = "report.pdf"

print(file.endswith(".pdf"))
```

Output:

```
True
```

---

## `split()`

Splits a string into a list.

```python
sentence = "Python SQL Azure"

print(sentence.split())
```

Output:

```
['Python', 'SQL', 'Azure']
```

---

## `join()`

Joins elements of a list into a single string.

```python
words = ["Python", "SQL", "Azure"]

print(" | ".join(words))
```

Output:

```
Python | SQL | Azure
```

---

# Formatted Strings (f-Strings)

An f-string provides a clean and readable way to include variables inside strings.

```python
name = "Arsalan"
course = "Python"

print(f"My name is {name}.")
print(f"I am learning {course}.")
```

Output:

```
My name is Arsalan.
I am learning Python.
```

---

# Difference Between `find()` and `index()`

| `find()`                  | `index()`                          |
| ------------------------- | ---------------------------------- |
| Returns `-1` if not found | Raises `ValueError` if not found   |
| Safer for searches        | Best when the substring must exist |

Example:

```python
text = "Python"

print(text.find("x"))
# Output: -1

print(text.index("x"))
# ValueError
```

---

# Important Points

* Strings are immutable (cannot be changed after creation).
* Indexing starts from `0`.
* Negative indexing starts from `-1`.
* Slicing extracts part of a string.
* `len()` returns the total number of characters.
* String methods return a new string and do not modify the original string.

---

# Summary

In this lesson, you learned:

* Creating Strings
* Indexing
* Slicing
* String Concatenation
* String Repetition
* Membership Operators
* Common String Methods
* f-Strings
* Difference between `find()` and `index()`

Strings are one of the most frequently used data types in Python and are essential for handling text in real-world applications.

---

# Homework

* Practice every string method with your own examples.
* Create a Student Profile Formatter.
* Count characters and words in a sentence.
* Check whether an email ends with `@gmail.com`.
* Replace words using `replace()`.
* Practice indexing and slicing with different strings.
* Push your work to GitHub with the commit message:

```
Day 05 - Strings Completed
```
