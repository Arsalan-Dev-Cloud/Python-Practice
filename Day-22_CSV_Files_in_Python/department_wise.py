import csv

file_path = "E:/Python-Practice/Day-22_CSV_Files_in_Python/employees.csv"

with open(file_path, "r", newline="") as file:

    data = csv.reader(file)

    next(data)

    department_count = {}

    total_employees = 0

    for row in data:

        department = row[2]

        if department in department_count:
            department_count[department] += 1 # department_count[department] = department_count[department] + 1
        else:
            department_count[department] = 1

        total_employees += 1  # total_employees = total_employees + 1

    print("=" * 20, "DEPARTMENT SUMMARY", "=" * 20)

    for department, count in department_count.items():

        print(f"{department}: {count} Employees")

    print("-" * 55)
    print("Total Employees:", total_employees)