#-------------- Methods for dictionary -----------------
student = {
    "name": "Arsalan",
    "age": 22,
    "city": "Latur"
}

print(student) # {'name': 'Arsalan', 'age': 22, 'city': 'Latur'}
print(len(student)) # 3

# Key():- 
print(student.keys()) # dict_keys(['name', 'age', 'city'])

# Value():-
print(student.values()) # dict_values(['Arsalan', 22, 'Latur'])

# Items():-
print(student.items()) # dict_items([('name', 'Arsalan'), ('age', 22), ('city', 'Latur')])

# update():-
student.update({"city":"Pune"})
print(student) # {'name': 'Arsalan', 'age': 22, 'city': 'Pune'}

# copy():-
new_student = student.copy()
print(new_student) # {'name': 'Arsalan', 'age': 22, 'city': 'Pune'}
