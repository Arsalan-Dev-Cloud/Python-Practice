#-------------- Methods for dictionary -----------------
student = {
    "name": "Arsalan",
    "age": 22,
    "city": "Latur"
}

print(student) # {'name': 'Arsalan', 'age': 22, 'city': 'Latur'}
print(len(student)) # 3


# Adding New Items:-
student["course"] = "Python"
print(student) #{'name': 'Arsalan', 'age': 22, 'city': 'Latur', 'course': 'Python'}

# Updating Values:-
student["age"] = 25
print(student) # {'name': 'Arsalan', 'age': 25, 'city': 'Latur', 'course': 'Python'}


# Removing Items:-

# 1. pop()
student.pop("city")
print(student) # {'name': 'Arsalan', 'age': 25, 'course': 'Python'}

# 2. del
del student["age"]
print(student) # {'name': 'Arsalan', 'course': 'Python'}

# 3. clear() - it removes every thing.
student.clear()
print(student) # {}
