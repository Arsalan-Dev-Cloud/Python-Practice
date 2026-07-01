# Day 04 – Operators 🐍

## 📌 What is an Operator?

An **operator** is a symbol that performs an operation on one or more values (called operands).

Example:

```python
a = 10
b = 5

print(a + b)
```

Output:

```
15
```

---

# 1. Arithmetic Operators

Arithmetic operators are used to perform mathematical calculations.

| Operator | Description         | Example   | Result |
| -------- | ------------------- | --------- | ------ |
| `+`      | Addition            | `10 + 5`  | `15`   |
| `-`      | Subtraction         | `10 - 5`  | `5`    |
| `*`      | Multiplication      | `10 * 5`  | `50`   |
| `/`      | Division            | `10 / 5`  | `2.0`  |
| `//`     | Floor Division      | `10 // 3` | `3`    |
| `%`      | Modulus (Remainder) | `10 % 3`  | `1`    |
| `**`     | Exponent (Power)    | `2 ** 3`  | `8`    |

### Example

```python
a = 20
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)
```

---

# 2. Assignment Operators

Assignment operators assign or update the value of a variable.

| Operator | Example   | Equivalent To |
| -------- | --------- | ------------- |
| `=`      | `x = 10`  | Assign value  |
| `+=`     | `x += 5`  | `x = x + 5`   |
| `-=`     | `x -= 5`  | `x = x - 5`   |
| `*=`     | `x *= 2`  | `x = x * 2`   |
| `/=`     | `x /= 2`  | `x = x / 2`   |
| `//=`    | `x //= 2` | `x = x // 2`  |
| `%=`     | `x %= 3`  | `x = x % 3`   |
| `**=`    | `x **= 2` | `x = x ** 2`  |

### Example

```python
x = 10

x += 5
print(x)

x *= 2
print(x)
```

---

# 3. Comparison Operators

Comparison operators compare two values and return either `True` or `False`.

| Operator | Meaning                  |
| -------- | ------------------------ |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |
| `>`      | Greater than             |
| `<`      | Less than                |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to    |

### Example

```python
a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
```

Output:

```
False
True
False
True
```

---

# 4. Logical Operators

Logical operators combine multiple conditions.

| Operator | Description                                      |
| -------- | ------------------------------------------------ |
| `and`    | Returns `True` if both conditions are true       |
| `or`     | Returns `True` if at least one condition is true |
| `not`    | Reverses the result                              |

### Example

```python
age = 22
salary = 30000

print(age > 18 and salary > 25000)
print(age > 30 or salary > 25000)
print(not(age > 18))
```

---

# 5. Identity Operators

Identity operators check whether two variables refer to the **same object in memory**.

| Operator | Meaning                                 |
| -------- | --------------------------------------- |
| `is`     | Both variables refer to the same object |
| `is not` | Variables refer to different objects    |

### Example

```python
a = [1, 2]
b = a
c = [1, 2]

print(a is b)
print(a is c)
```

Output:

```
True
False
```

> **Note:** `==` compares values, while `is` compares object identity (memory reference).

---

# 6. Membership Operators

Membership operators check whether a value exists in a sequence such as a string, list, tuple, or dictionary.

| Operator | Meaning              |
| -------- | -------------------- |
| `in`     | Value exists         |
| `not in` | Value does not exist |

### Example

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

# 7. Operator Precedence

Python evaluates operators in the following order:

1. `()` Parentheses
2. `**` Exponent
3. `*`, `/`, `//`, `%`
4. `+`, `-`
5. Comparison Operators (`==`, `!=`, `>`, `<`, `>=`, `<=`)
6. `not`
7. `and`
8. `or`

### Example

```python
result = 5 + 3 * 2
print(result)
```

Output:

```
11
```

Because multiplication is performed before addition.

Using parentheses:

```python
result = (5 + 3) * 2
print(result)
```

Output:

```
16
```

---

# Difference Between `/` and `//`

```python
print(10 / 3)
print(10 // 3)
```

Output:

```
3.3333333333333335
3
```

* `/` returns the exact decimal result.
* `//` returns the integer part (floor division).

---

# Important Points

* Arithmetic operators perform mathematical calculations.
* Assignment operators update variable values.
* Comparison operators always return `True` or `False`.
* Logical operators combine multiple conditions.
* Identity operators compare object identity, not values.
* Membership operators check whether a value exists in a collection.
* Operator precedence determines the order of evaluation.

---

# Summary

In this lesson, you learned:

* Arithmetic Operators
* Assignment Operators
* Comparison Operators
* Logical Operators
* Identity Operators
* Membership Operators
* Operator Precedence

These operators are used in almost every Python program, from simple scripts to large applications.

---

# Homework

* Practice each operator with at least three examples.
* Build a simple calculator using arithmetic operators.
* Compare different numbers using comparison operators.
* Write programs using `and`, `or`, and `not`.
* Experiment with `is` vs `==`.
* Check membership in strings and lists using `in` and `not in`.
