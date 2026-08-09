# 🐍 Day 15 – Advanced Functions & Lambda Functions

Welcome to **Day 15 of Python Daily Practice**.

In this lesson, I practiced advanced Python function concepts including `*args`, `**kwargs`, lambda functions, `map()`, and `filter()`.

---

## 📚 Topics Covered

* Default Arguments
* Keyword Arguments
* `*args`
* `**kwargs`
* Argument Unpacking
* Dictionary Unpacking
* Lambda Functions
* `map()`
* `filter()`
* Functions with Lists and Dictionaries
* Employee Salary Analyzer Challenge

---

## 📂 Folder Structure

```text
Day-15_Advanced_Functions/
│
├── default_arguments.py
├── args.py
├── kwargs.py
├── lambda_functions.py
├── map_filter.py
├── examples.py
├── challenge.py
├── notes.md
└── README.md
```

---

# 🔹 Default Arguments

Default arguments allow a function to use a predefined value when no argument is provided.

```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()
greet("Arsalan")
```

Output:

```text
Hello, Guest!
Hello, Arsalan!
```

---

# 🔹 Keyword Arguments

Keyword arguments allow values to be passed using parameter names.

```python
def student(name, course, marks):
    print(name)
    print(course)
    print(marks)

student(
    marks=90,
    name="Arsalan",
    course="Big Data"
)
```

When keyword arguments are used, the order of the arguments does not have to match the parameter order.

---

# 🔹 `*args`

`*args` allows a function to accept multiple positional arguments.

```python
def total_marks(*marks):
    return sum(marks)

print(total_marks(90, 85, 95, 80))
```

Inside the function, `marks` is stored as a **tuple**.

```text
*args → Multiple positional arguments → Tuple
```

---

# 🔹 `**kwargs`

`**kwargs` allows a function to accept multiple keyword arguments.

```python
def employee(**details):
    for key, value in details.items():
        print(f"{key:<10}: {value}")

employee(
    name="Arsalan",
    salary=60000
)
```

Inside the function, `details` is stored as a **dictionary**.

```text
**kwargs → Multiple keyword arguments → Dictionary
```

---

# 🔹 Argument Unpacking

A list or tuple can be unpacked using `*`.

```python
salaries = [60000, 45000, 75000, 35000]

def total_salary(*salaries):
    return sum(salaries)

print(total_salary(*salaries))
```

Here:

```python
*salaries
```

unpacks:

```text
[60000, 45000, 75000, 35000]
```

into:

```text
60000, 45000, 75000, 35000
```

---

# 🔹 Dictionary Unpacking

A dictionary can be unpacked using `**`.

```python
employee = {
    "name": "Arsalan",
    "salary": 60000
}

def display_employee(**details):
    print(details)

display_employee(**employee)
```

The dictionary:

```python
{
    "name": "Arsalan",
    "salary": 60000
}
```

is unpacked into:

```text
name="Arsalan"
salary=60000
```

---

# 🔹 Lambda Functions

A lambda is a small anonymous function.

Normal function:

```python
def square(number):
    return number ** 2
```

Lambda version:

```python
square = lambda number: number ** 2

print(square(5))
```

Output:

```text
25
```

Lambda syntax:

```text
lambda arguments: expression
```

---

# 🔹 `map()`

`map()` applies a function to every item in an iterable.

```python
numbers = [1, 2, 3, 4, 5]

squares = list(
    map(lambda number: number ** 2, numbers)
)

print(squares)
```

Output:

```text
[1, 4, 9, 16, 25]
```

Easy way to remember:

```text
map() → Transform items
```

---

# 🔹 `filter()`

`filter()` selects items that satisfy a condition.

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(
    filter(lambda number: number % 2 == 0, numbers)
)

print(even_numbers)
```

Output:

```text
[2, 4, 6]
```

Easy way to remember:

```text
filter() → Select items
```

---

# 🔹 `map()` vs `filter()`

| Function   | Purpose               |
| ---------- | --------------------- |
| `map()`    | Transform every item  |
| `filter()` | Select matching items |

Example:

```text
map()

[1, 2, 3]
     ↓
[1, 4, 9]


filter()

[1, 2, 3, 4]
     ↓
[2, 4]
```

---

# 💼 Day 15 Challenge – Employee Salary Analyzer

The challenge used the following employee data:

```python
employees = [
    {"name": "Arsalan", "salary": 60000},
    {"name": "Ali", "salary": 45000},
    {"name": "Shoaib", "salary": 75000},
    {"name": "Ahmed", "salary": 35000}
]
```

The program performs several operations on the employee information.

---

## 1️⃣ Filter Employees by Salary

Employees earning at least ₹50,000 are selected using `filter()` and `lambda`.

```python
condition_salary = list(
    filter(
        lambda employee: employee["salary"] >= 50000,
        employees
    )
)

print(condition_salary)
```

---

## 2️⃣ Increase Salary by 10%

Salary increase formula:

```text
New Salary = Salary + (Salary × 10 / 100)
```

Implemented using `map()`:

```python
salary_increase = list(
    map(
        lambda employee:
        employee["salary"] +
        (employee["salary"] * 10 / 100),
        employees
    )
)

print(salary_increase)
```

Example:

```text
60000
  ↓ +10%
66000
```

---

## 3️⃣ Calculate Total Salaries Using `*args`

First, salary values are extracted:

```python
salaries = []

for employee in employees:
    salaries.append(employee["salary"])
```

Result:

```python
[60000, 45000, 75000, 35000]
```

Then:

```python
def total_salary(*salaries):
    return sum(salaries)

print(total_salary(*salaries))
```

Output:

```text
215000
```

---

## 4️⃣ Display Employee Information Using `**kwargs`

```python
def display_employee(**details):
    for key, value in details.items():
        print(f"{key:<10}: {value}")
```

Display all employees:

```python
for employee in employees:
    display_employee(**employee)
    print()
```

Example output:

```text
name      : Arsalan
salary    : 60000

name      : Ali
salary    : 45000

name      : Shoaib
salary    : 75000

name      : Ahmed
salary    : 35000
```

---

# 🧠 Important Concepts Learned

### `*args`

```text
Multiple positional arguments
          ↓
         Tuple
```

Example:

```python
def demo(*args):
    print(args)

demo(10, 20, 30)
```

Output:

```text
(10, 20, 30)
```

---

### `**kwargs`

```text
Multiple keyword arguments
          ↓
       Dictionary
```

Example:

```python
def demo(**kwargs):
    print(kwargs)

demo(name="Arsalan", salary=60000)
```

Output:

```text
{'name': 'Arsalan', 'salary': 60000}
```

---

# 🔄 Collecting vs Unpacking

One of the most important concepts from today's challenge:

### Collecting

```python
def total(*numbers):
```

`*numbers` collects multiple positional arguments.

```python
def employee(**details):
```

`**details` collects multiple keyword arguments.

### Unpacking

```python
total(*numbers)
```

`*numbers` unpacks a list/tuple into separate positional arguments.

```python
employee(**details)
```

`**details` unpacks a dictionary into keyword arguments.

---

# 📊 Concepts Combined in Today's Challenge

```text
Lists
  │
  ▼
Dictionaries
  │
  ▼
Loops
  │
  ▼
Functions
  │
  ├──── *args
  │
  └──── **kwargs
  │
  ▼
Lambda
  │
  ├──── map()
  │
  └──── filter()
  │
  ▼
Employee Salary Analyzer
```

---

# 💡 Key Takeaways

* `*args` collects multiple positional arguments into a tuple.
* `**kwargs` collects multiple keyword arguments into a dictionary.
* `*` can also unpack lists and tuples.
* `**` can unpack dictionaries.
* Lambda functions are useful for small operations.
* `map()` transforms iterable items.
* `filter()` selects items based on a condition.
* Normal functions are usually better when logic becomes complex.

---

# 🎯 Practice Tasks

* Create functions using `*args`.
* Create functions using `**kwargs`.
* Practice unpacking lists using `*`.
* Practice unpacking dictionaries using `**`.
* Create lambda functions.
* Practice `map()` with numbers.
* Practice `filter()` with conditions.
* Complete the Employee Salary Analyzer.

---

# 📝 Git Commit

After completing Day 15:

```bash
git add .
git commit -m "Day 15 - Advanced Functions and Lambda Completed"
git push
```

---

# ✅ Day 15 Completed

Topics completed:

```text
✔ Default Arguments
✔ Keyword Arguments
✔ *args
✔ **kwargs
✔ Argument Unpacking
✔ Dictionary Unpacking
✔ Lambda Functions
✔ map()
✔ filter()
✔ Employee Salary Analyzer
```

> **Day 15 taught how Python functions can accept flexible arguments and how lambda, map, and filter can be used to process collections efficiently.**
