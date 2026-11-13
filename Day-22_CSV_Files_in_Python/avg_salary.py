
import csv

file_path = "E:/Python-Practice/Day-22_CSV_Files_in_Python/employees.csv"

department_x = input("Enter Department: ")

employee_x = []

salary = 0
employee_count = 0
found = False

try:
    with open(file_path, "r", newline="") as file:

        data = csv.reader(file)
        next(data)

        for row in data:

            if row[2].lower() == department_x.lower():

                employee_x.append(row[1])
                employee_count += 1
                found = True

                dep_salary = int(row[3])
                salary += dep_salary

                print("=" * 40)
                print("Employee Name:", row[1])
                print("Department:", row[2])
                print("Salary:", row[3])

        if found:
            avg_salary = salary / employee_count

            print("-" * 40)
            print("Employees:", employee_count)
            print("Total Salary:", salary)
            print("Average Salary:", avg_salary)

        else:
            print("Department Not Found!!!")

except FileNotFoundError:
    print("File Not Found!!!")
