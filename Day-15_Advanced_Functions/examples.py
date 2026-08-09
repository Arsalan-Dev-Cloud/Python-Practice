# ==========================================
# Day 15 - Advanced Functions & Lambda
# examples.py
# ==========================================


# ------------------------------------------
# Example 1: Default Arguments
# ------------------------------------------

print("----- Example 1: Default Arguments -----")

def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()
greet("Arsalan")


# ------------------------------------------
# Example 2: Keyword Arguments
# ------------------------------------------

print("\n----- Example 2: Keyword Arguments -----")

def student(name, course, marks):
    print(f"Name   : {name}")
    print(f"Course : {course}")
    print(f"Marks  : {marks}")

student(
    marks=90,
    name="Arsalan",
    course="Big Data"
)


# ------------------------------------------
# Example 3: *args
# ------------------------------------------

print("\n----- Example 3: *args -----")

def total_marks(*marks):
    print("Marks :", marks)
    print("Total :", sum(marks))

total_marks(90, 85, 95, 80, 88)


# ------------------------------------------
# Example 4: Loop with *args
# ------------------------------------------

print("\n----- Example 4: Loop with *args -----")

def show_skills(*skills):
    for skill in skills:
        print(skill)

show_skills(
    "Python",
    "SQL",
    "React",
    "FastAPI"
)


# ------------------------------------------
# Example 5: **kwargs
# ------------------------------------------

print("\n----- Example 5: **kwargs -----")

def employee(**details):
    print(details)

employee(
    Name="Arsalan",
    Department="Data Engineering",
    Salary=60000
)


# ------------------------------------------
# Example 6: Loop with **kwargs
# ------------------------------------------

print("\n----- Example 6: Loop with **kwargs -----")

def show_employee(**details):
    for key, value in details.items():
        print(f"{key:<12}: {value}")

show_employee(
    Name="Arsalan",
    Department="Data Engineering",
    Salary=60000,
    City="Pune"
)


# ------------------------------------------
# Example 7: Lambda Function
# ------------------------------------------

print("\n----- Example 7: Lambda -----")

square = lambda number: number ** 2

print("Square of 5:", square(5))


# ------------------------------------------
# Example 8: Lambda with Multiple Arguments
# ------------------------------------------

print("\n----- Example 8: Lambda Addition -----")

add = lambda a, b: a + b

print("10 + 20 =", add(10, 20))


# ------------------------------------------
# Example 9: map() + lambda
# ------------------------------------------

print("\n----- Example 9: map() -----")

numbers = [1, 2, 3, 4, 5]

squares = list(
    map(lambda number: number ** 2, numbers)
)

print("Original :", numbers)
print("Squares  :", squares)


# ------------------------------------------
# Example 10: filter() + lambda
# ------------------------------------------

print("\n----- Example 10: filter() -----")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(
    filter(lambda number: number % 2 == 0, numbers)
)

print("Numbers :", numbers)
print("Even    :", even_numbers)


# ------------------------------------------
# Example 11: Student Marks
# ------------------------------------------

print("\n----- Example 11: Student Marks -----")

marks = [45, 92, 78, 33, 85, 25]

passed = list(
    filter(lambda mark: mark >= 35, marks)
)

updated_marks = list(
    map(lambda mark: mark + 5, marks)
)

print("Original Marks :", marks)
print("Passed Marks   :", passed)
print("Updated Marks  :", updated_marks)


print("\n----- All Examples Completed -----")