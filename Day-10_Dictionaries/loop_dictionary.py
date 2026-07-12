student = {
    "name": "Arsalan",
    "age": 22,
    "city": "Latur"
}

# Loop through keys:
for key in student:
    print(key)
"""
name
age
city
"""

for value in student.values():
    print(value)
"""
Arsalan
22
Latur
"""

for key, value in student.items():
    print(key, ":", value)
"""
name : Arsalan
age : 22
city : Latur
"""
