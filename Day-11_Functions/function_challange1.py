# -------- Student Result System using Functions --------

def input_marks():
    print("Enter the Marks Below")

    marks = {
        "English": int(input("English   : ")),
        "Maths": int(input("Maths     : ")),
        "Physics": int(input("Physics   : ")),
        "Chemistry": int(input("Chemistry : ")),
        "Biology": int(input("Biology   : ")),
        "Geography": int(input("Geography : ")),
        "Civic": int(input("Civic     : "))
    }

    return marks


def calculate_total(marks):
    total = sum(marks.values())
    return total


def calculate_average(total, no_of_subjects):
    average = total / no_of_subjects
    return average


def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def display_report(marks, total, average, grade):
    print("\n----------- Student Report Card -----------")

    for subject, mark in marks.items():
        print(f"{subject:<12}: {mark}")

    print("-" * 35)
    print(f"{'Total':<12}: {total}")
    print(f"{'Average':<12}: {average:.2f}")
    print(f"{'Grade':<12}: {grade}")


# ---------------- Main Program ----------------

marks = input_marks()

total = calculate_total(marks)

average = calculate_average(total, len(marks))

grade = calculate_grade(average)

display_report(marks, total, average, grade)




# Output:-
"""
Enter the Marks Below
English   : 60
Maths     : 60
Physics   : 60
Chemistry : 60
Biology   : 60
Geography : 60
Civic     : 60

----------- Student Report Card -----------
English     : 60
Maths       : 60
Physics     : 60
Chemistry   : 60
Biology     : 60
Geography   : 60
Civic       : 60
-----------------------------------
Total       : 420
Average     : 60.00
Grade       : D
"""
