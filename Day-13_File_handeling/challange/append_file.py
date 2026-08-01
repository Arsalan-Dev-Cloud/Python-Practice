student = {
    "Name": input("Enter the Name : "),
    "Roll No.": input("Enter the Roll No : "),
    "Course": input("Enter the Course : "),
    "Marks": input("Enter the Marks :")
}

with open("Student.txt", "a") as file:
    for key, value in student.items():
        file.write(f"{key:<10}: {value}\n")

    file.write("\n")  # Add a newline after each student's data for better readability