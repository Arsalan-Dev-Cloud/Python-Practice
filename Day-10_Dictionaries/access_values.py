#-------------- Access Values -----------------
student = {
    "name": "Arsalan",
    "age": 22,
    "city": "Latur"
}

print(student["name"]) # Arsalan
print(student["age"]) # 22

# using get() function
print(student.get("city")) # Latur
print(student.get("salary")) # None

# without get() function
print(student["salary"]) # keyError

# get() function is the safe.
