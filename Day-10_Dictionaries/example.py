# ----------- Real world example -----------
student = {
    "Name": "Arsalan",
    "Age": 22,
    "Course": "Python",
    "City": "Latur"
}

print("-------- Student Profile --------")

for key, value in student.items():
    print(f"{key:<10}: {value}")


# Ouput -
-------- Student Profile --------
Name      : Arsalan
Age       : 22
Course    : Python
City      : Latur
