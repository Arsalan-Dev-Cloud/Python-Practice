# Day 07 – Loops 🐍

## 📌 What is a Loop?

A **loop** is used to execute a block of code repeatedly without writing the same code multiple times.

Loops help automate repetitive tasks and make programs shorter, cleaner, and more efficient.

### Example Without a Loop

```python
print("Welcome")
print("Welcome")
print("Welcome")
print("Welcome")
print("Welcome")
```

### Example With a Loop

```python
for i in range(5):
    print("Welcome")
```

Output:

```
Welcome
Welcome
Welcome
Welcome
Welcome
```

---

# Why Do We Use Loops?

Loops are useful when:

* Printing numbers from 1 to 1000.
* Reading multiple user inputs.
* Processing CSV or Excel data.
* Iterating through lists, strings, or dictionaries.
* Repeating tasks automatically.

---

# Types of Loops in Python

Python provides two types of loops:

1. `for` Loop
2. `while` Loop

---

# 1. The `for` Loop

The `for` loop is used when the number of iterations is known.

## Syntax

```python
for variable in sequence:
    # code
```

### Example

```python
for i in range(5):
    print(i)
```

Output:

```
0
1
2
3
4
```

---

# The `range()` Function

The `range()` function generates a sequence of numbers.

## `range(stop)`

```python
for i in range(5):
    print(i)
```

Output:

```
0
1
2
3
4
```

---

## `range(start, stop)`

```python
for i in range(1, 6):
    print(i)
```

Output:

```
1
2
3
4
5
```

---

## `range(start, stop, step)`

```python
for i in range(2, 11, 2):
    print(i)
```

Output:

```
2
4
6
8
10
```

---

## Reverse Loop

```python
for i in range(10, 0, -1):
    print(i)
```

Output:

```
10
9
8
7
6
5
4
3
2
1
```

---

# Loop Through a String

```python
name = "Arsalan"

for letter in name:
    print(letter)
```

Output:

```
A
r
s
a
l
a
n
```

---

# Loop Through a List

```python
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)
```

Output:

```
Apple
Banana
Mango
```

---

# 2. The `while` Loop

A `while` loop repeats as long as the condition is `True`.

## Syntax

```python
while condition:
    # code
```

### Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output:

```
1
2
3
4
5
```

---

# Infinite Loop

```python
while True:
    print("Hello")
```

⚠️ This loop never ends unless it is stopped using `break` or interrupted manually.

---

# The `break` Statement

The `break` statement immediately exits a loop.

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

Output:

```
0
1
2
3
4
```

---

# The `continue` Statement

The `continue` statement skips the current iteration and moves to the next one.

```python
for i in range(6):
    if i == 3:
        continue
    print(i)
```

Output:

```
0
1
2
4
5
```

---

# The `pass` Statement

The `pass` statement is a placeholder. It performs no action.

```python
for i in range(5):
    if i == 2:
        pass
    print(i)
```

Output:

```
0
1
2
3
4
```

---

# Nested Loops

A nested loop is a loop inside another loop.

```python
for i in range(3):
    for j in range(3):
        print(i, j)
```

Output:

```
0 0
0 1
0 2
1 0
1 1
1 2
2 0
2 1
2 2
```

---

# Pattern Printing Example

```python
for i in range(5):
    print("*" * (i + 1))
```

Output:

```
*
**
***
****
*****
```

---

# Real-World Examples

## Print Numbers from 1 to 10

```python
for i in range(1, 11):
    print(i)
```

---

## Sum of Numbers

```python
total = 0

for i in range(1, 6):
    total += i

print(total)
```

Output:

```
15
```

---

## Multiplication Table

```python
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
```

---

## Countdown Timer

```python
count = 10

while count > 0:
    print(count)
    count -= 1

print("Lift Off! 🚀")
```

---

# `for` vs `while`

| `for` Loop                                   | `while` Loop                                   |
| -------------------------------------------- | ---------------------------------------------- |
| Used when the number of iterations is known. | Used when the number of iterations is unknown. |
| Iterates over a sequence or `range()`.       | Runs until a condition becomes `False`.        |
| Best for fixed repetitions.                  | Best for user input and menus.                 |

---

# Important Points

* Use `for` when you know how many times the loop should run.
* Use `while` when the number of iterations is unknown.
* `break` exits a loop immediately.
* `continue` skips the current iteration.
* `pass` is a placeholder.
* Nested loops are useful for patterns and working with rows and columns.
* Always update the condition in a `while` loop to avoid infinite loops.

---

# Summary

In this lesson, you learned:

* What loops are
* `for` Loop
* `while` Loop
* `range()` Function
* Looping through strings and lists
* `break`
* `continue`
* `pass`
* Nested Loops
* Pattern Printing
* Real-world loop examples

Loops are one of the most important programming concepts and are widely used in data processing, automation, web development, scripting, and Data Engineering.

---

# Homework

* Practice every loop example.
* Print even and odd numbers using loops.
* Create multiplication tables.
* Find the sum of numbers from 1 to 100.
* Create a countdown timer.
* Build the Number Guessing Game using a `while` loop.
* Push your work to GitHub.
