subjects = [
    "English",
    "Maths",
    "Physics",
    "Chemistry",
    "Biology",
    "Geography",
    "Civic"
]


def input_marks():
    marks = {}

    print("Enter Marks")

    for subject in subjects:
        marks[subject] = int(input(f"{subject:<10}: "))

    return marks


def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    return "F"


marks = input_marks()

total = sum(marks.values())
average = total / len(marks)
grade = calculate_grade(average)

print("\n------ Student Report ------")

for subject, mark in marks.items():
    print(f"{subject:<12}: {mark}")

print("-" * 30)
print(f"{'Total':<12}: {total}")
print(f"{'Average':<12}: {average:.2f}")
print(f"{'Grade':<12}: {grade}")



# Output:-

"""
Enter Marks
English   : 60
Maths     : 60
Physics   : 60
Chemistry : 60
Biology   : 60
Geography : 60
Civic     : 60

------ Student Report ------
English     : 60
Maths       : 60
Physics     : 60
Chemistry   : 60
Biology     : 60
Geography   : 60
Civic       : 60
------------------------------
Total       : 420
Average     : 60.00
Grade       : D
"""
