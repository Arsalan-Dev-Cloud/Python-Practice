student = {
    "Name": "Arsalan",
    "Roll Number": 60,
    "Course": "Big Data",
    "Maths Marks": 95,
    "Science Marks": 90,
    "English Marks": 85
}

print("-----------Student Report Card------------")
for key, value in student.items():
    print(f"{key:<20}: {value}")

count =0
total =0
for key, value in student.items():
    if "Marks" in key:
        total += value
        count += 1

average = total/count

print(f"{'Total':<20}: {total}")
print(f"{'Avearge':<20}: {average:.2f}")

grades = {
    90: "A",
    80: "B",
    70: "C",
    60: "D",
    0: "F"
}

for marks in grades:
    if average >= marks:
        print(f"{'Grade':<20}: {grades[marks]}")
        break

# Output:
-----------Student Report Card------------
Name                : Arsalan
Roll Number         : 60
Course              : Big Data
Maths Marks         : 95
Science Marks       : 90
English Marks       : 85
Total               : 270
Avearge             : 90.00
Grade               : A
