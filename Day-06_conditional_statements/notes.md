# Day 06 – Conditional Statements 🐍

## 📌 What are Conditional Statements?

Conditional statements allow a program to make decisions based on whether a condition is **True** or **False**.

Example:

```python
age = 20

if age >= 18:
    print("You are eligible to vote.")
```

Output:

```
You are eligible to vote.
```

---

# Why Do We Need Conditional Statements?

Conditional statements help programs make decisions.

Examples:

* Check whether a student passed or failed.
* Verify a username and password.
* Determine voting eligibility.
* Check whether a number is even or odd.
* Calculate grades based on marks.

---

# 1. The `if` Statement

The `if` statement executes a block of code only when the condition is `True`.

### Syntax

```python
if condition:
    # code
```

### Example

```python
marks = 80

if marks >= 35:
    print("You passed the exam.")
```

Output:

```
You passed the exam.
```

---

# 2. The `if...else` Statement

The `else` block runs when the condition is `False`.

### Syntax

```python
if condition:
    # code
else:
    # code
```

### Example

```python
age = 16

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
```

Output:

```
Not eligible to vote
```

---

# 3. The `if...elif...else` Statement

Used when there are multiple conditions.

### Example

```python
marks = 72

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 35:
    print("Grade D")
else:
    print("Fail")
```

Output:

```
Grade C
```

---

# 4. Nested `if`

A nested `if` is an `if` statement inside another `if`.

```python
age = 25
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to vote")
    else:
        print("Not a citizen")
else:
    print("Underage")
```

---

# 5. Logical Operators

## `and`

Returns `True` only if **both** conditions are true.

```python
age = 25
salary = 30000

if age >= 21 and salary >= 25000:
    print("Loan Approved")
```

---

## `or`

Returns `True` if **at least one** condition is true.

```python
attendance = 80
medical_certificate = False

if attendance >= 75 or medical_certificate:
    print("Allowed to take exam")
```

---

## `not`

Reverses the result.

```python
is_logged_in = False

if not is_logged_in:
    print("Please log in")
```

---

# 6. Short-hand `if`

```python
age = 20

if age >= 18: print("Adult")
```

---

# 7. Ternary Operator

A shorter way to write an `if...else` statement.

```python
age = 20

status = "Adult" if age >= 18 else "Minor"

print(status)
```

Output:

```
Adult
```

---

# 8. Indentation

Python uses indentation instead of `{}`.

✅ Correct

```python
age = 18

if age >= 18:
    print("Eligible")
```

❌ Incorrect

```python
age = 18

if age >= 18:
print("Eligible")
```

This causes an `IndentationError`.

---

# Real-World Examples

## Voting Eligibility

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
```

---

## Even or Odd

```python
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

## Largest of Two Numbers

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("First number is larger.")
else:
    print("Second number is larger.")
```

---

## Grade Calculator

```python
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 35:
    print("Grade D")
else:
    print("Fail")
```

---

# Important Points

* Conditional statements control the flow of a program.
* Conditions always evaluate to either `True` or `False`.
* Use proper indentation.
* Only one block in an `if...elif...else` chain executes.
* `elif` can be used multiple times.
* `else` is optional.

---

# Summary

In this lesson you learned:

* `if`
* `if...else`
* `if...elif...else`
* Nested `if`
* Logical Operators (`and`, `or`, `not`)
* Short-hand `if`
* Ternary Operator
* Indentation
* Real-world examples

Conditional statements are the foundation of decision-making in Python and are used in almost every real-world application.

---

# Homework

* Practice every type of conditional statement.
* Solve all practice questions.
* Create a Grade Calculator.
* Create an ATM Login System.
* Push your work to GitHub.

Commit Message:

```
Day 06 - Conditional Statements Completed
```
