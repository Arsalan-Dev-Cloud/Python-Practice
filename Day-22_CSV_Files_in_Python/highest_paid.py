
import csv

file_path = "E:/Python-Practice/Day-22_CSV_Files_in_Python/employees.csv"

with open(file_path, "r", newline="") as file:

    data = csv.reader(file)
    next(data)

    salary_x = []
    employee_x = []

    for row in data:
        salary_x.append(int(row[3]))
        employee_x.append(row.copy())

    print("Salary List:", salary_x)

    highest_salary = 0
    highest_employee = []

    for i in range(len(salary_x)):

        count = 0

        for j in range(len(salary_x)):

            if salary_x[i] >= salary_x[j] and i != j:
                count += 1

        if count == len(salary_x) - 1:
            highest_salary = salary_x[i]
            highest_employee = employee_x[i].copy()

    print("\nHighest Employee Record:", highest_employee)

    print("\n" + "=" * 40)
    print("       HIGHEST-PAID EMPLOYEE")
    print("=" * 40)

    print("Employee ID:", highest_employee[0])
    print("Name:", highest_employee[1])
    print("Department:", highest_employee[2])
    print("Salary:", highest_employee[3])
