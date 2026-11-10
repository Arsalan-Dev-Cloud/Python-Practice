import csv

file_path = "E:/Python-Practice/Day-22_CSV_Files_in_Python/employees.csv"

with open(file_path, "r", newline="") as file:

    data = csv.reader(file)

    next(data)  # Skip header

    print("-" * 25, "Employee Records", "-" * 25)

    total_employees = 0

    for row in data:

        print("Employee ID:", row[0])
        print("Name:", row[1])
        print("Department:", row[2])
        print("Salary:", row[3])

        print("-" * 50)

        total_employees += 1

    print("Total Employees:", total_employees)