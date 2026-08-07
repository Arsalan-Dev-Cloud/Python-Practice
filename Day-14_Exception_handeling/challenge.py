# ==========================================
# Day 14 Challenge - Exception Handling
# Student Record System
# ==========================================

try:
    # Take student information
    name = input("Enter Name     : ")
    roll_no = int(input("Enter Roll No. : "))
    course = input("Enter Course   : ")
    marks = int(input("Enter Marks    : "))

    # Validate marks
    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")

    # Store information in dictionary
    student = {
        "Name": name,
        "Roll No.": roll_no,
        "Course": course,
        "Marks": marks
    }

    # Save student information
    with open("Student.txt", "a") as file:
        for key, value in student.items():
            file.write(f"{key:<10}: {value}\n")

        file.write("\n")


except ValueError as error:
    print(f"\nInvalid Input: {error}")


except OSError as error:
    print(f"\nFile Error: {error}")


else:
    print("\nStudent record saved successfully!")


finally:
    print("Program finished.")