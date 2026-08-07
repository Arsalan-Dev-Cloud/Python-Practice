#-----------File Exception Handling in Python----------------

with open("Student.txt", "r") as file:
    print(file.read()) # FileNotFoundError

try:
    with open("Student.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("Student.txt does not exist.")