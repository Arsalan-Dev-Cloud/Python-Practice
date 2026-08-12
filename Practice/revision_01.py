# Write a program that asks the user for:
"""
Name
Age
Course
Python Marks
SQL Marks
"""

# Then calculate the total and average of Python and SQL marks.

# Use only this things: -
"""
input()
int()
variables
+
/
f-string
:.2f
"""


# Program ------------------------------------------------------------->

Name = input("Enter Your Name: ")
Age = int(input("Enter Your Age: "))
Course = input("Enter Your Course: ")
Python_marks = int(input("Enter the Python Marks:"))
SQL_marks = int(input("Enter the SQL Marks: "))

print("*************Information************")
print(f"{'Name':<20}: {Name}")
print(f"{'Age':<20}: {Age}")
print(f"{'Course':<20}: {Course}")
print(f"{'Python Marks':<20}: {Python_marks}")
print(f"{'SQL Marks':<20}: {SQL_marks}")
print(f"{'Total':<20}: {Python_marks + SQL_marks}")
print(f"{'Average':<20}: {(Python_marks + SQL_marks) / 2:.2f}")