#------------Raise Exception----------------

age = int(input("Enter age: "))

if age < 0:
    raise ValueError("Age cannot be negative.")

print("Age:", age)

"""
Input:- -5
Output:- ValueError: Age cannot be negative.
"""