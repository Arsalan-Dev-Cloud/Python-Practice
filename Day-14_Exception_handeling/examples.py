# ==========================================
# Day 14 - Exception Handling
# examples.py
# ==========================================


# ------------------------------------------
# Example 1: Basic try-except
# ------------------------------------------

print("----- Example 1: Basic try-except -----")

try:
    number = int(input("Enter a number: "))
    print("You entered:", number)

except ValueError:
    print("Invalid input! Please enter a number.")


# ------------------------------------------
# Example 2: Multiple Exceptions
# ------------------------------------------

print("\n----- Example 2: Multiple Exceptions -----")

try:
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print("Result:", result)

except ValueError:
    print("Invalid input! Enter numbers only.")

except ZeroDivisionError:
    print("Cannot divide by zero!")


# ------------------------------------------
# Example 3: else
# ------------------------------------------

print("\n----- Example 3: else -----")

try:
    age = int(input("Enter your age: "))

except ValueError:
    print("Age must be a number.")

else:
    print("Your age is:", age)


# ------------------------------------------
# Example 4: finally
# ------------------------------------------

print("\n----- Example 4: finally -----")

try:
    number = int(input("Enter a number: "))
    print("Number:", number)

except ValueError:
    print("Invalid number.")

finally:
    print("This line always runs.")


# ------------------------------------------
# Example 5: FileNotFoundError
# ------------------------------------------

print("\n----- Example 5: File Handling -----")

try:
    with open("Student.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("Student.txt was not found.")


# ------------------------------------------
# Example 6: IndexError
# ------------------------------------------

print("\n----- Example 6: IndexError -----")

numbers = [10, 20, 30]

try:
    print(numbers[5])

except IndexError:
    print("That index does not exist.")


# ------------------------------------------
# Example 7: KeyError
# ------------------------------------------

print("\n----- Example 7: KeyError -----")

student = {
    "Name": "Arsalan",
    "Marks": 90
}

try:
    print(student["Course"])

except KeyError:
    print("That key does not exist.")


# ------------------------------------------
# Example 8: Get Actual Error Message
# ------------------------------------------

print("\n----- Example 8: Exception Message -----")

try:
    number = int(input("Enter number: "))
    result = 100 / number

except Exception as error:
    print("Error:", error)

else:
    print("Result:", result)


# ------------------------------------------
# Example 9: raise
# ------------------------------------------

print("\n----- Example 9: raise -----")

try:
    marks = int(input("Enter marks: "))

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")

    print("Marks:", marks)

except ValueError as error:
    print("Error:", error)


print("\n----- All Examples Completed -----")



"""
try
 │
 ├── Error occurs ─────→ except
 │
 └── No error ─────────→ else
                          │
                          ▼
                       finally

                       

try      → Code that might cause an error
except   → Handle the error
else     → Runs when there is no error
finally  → Runs every time
raise    → Manually create an exception
"""