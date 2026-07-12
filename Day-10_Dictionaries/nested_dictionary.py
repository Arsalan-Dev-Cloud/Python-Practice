#------------ Nested Dictionary -------------
students = {
    "student1": {
        "name": "Ali",
        "marks": 85
    },
    "student2":{
        "name": "Arsalan",
        "marks" : 92
    }
}

print(students["student2"]["marks"]) # 93
print(students["student1"]["name"]) # Ali
