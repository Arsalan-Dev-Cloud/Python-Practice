import csv

file_path = "E:/Python-Practice/Day-22_CSV_Files_in_Python/CSV-Files/employees.csv"

with open(file_path, "r", newline="", encoding= "utf-8-sig") as file:
    data = csv.DictReader(file)

    salary_x = []
    highest_salary = 0
    lowest_salary = 0
    high_emp = []
    low_emp = []
    emp_count = 0
    total_salary = 0

    for row in data:
        salary_x.append(int(row['Salary']))
        emp_count += 1

    for i in range(len(salary_x)):

        high_count = 0
        low_count = 0

        for j in range(len(salary_x)):

            if salary_x[i] >= salary_x[j] and i != j:
                high_count += 1

            if salary_x[i] <= salary_x[j] and i != j:
                low_count += 1

        if high_count == len(salary_x) - 1:
            highest_salary = salary_x[i]

        if low_count == len(salary_x) - 1:
            lowest_salary = salary_x[i]

    for salary in salary_x:
        total_salary += salary

    avg_salary = total_salary / emp_count


    file.seek(0)
    data = csv.DictReader(file)

    for row in data:
        if int(row['Salary']) == highest_salary:
            high_emp.append(row.copy())

        if int(row['Salary']) == lowest_salary:
            low_emp.append(row.copy())


    print("=" * 15, "CSV File Result", "=" * 15)
    print(f"\n{'Result':<20} {'Employee':<20} {'Salary':<20}")
    print("-" * 50)
    print(f"{'Highest':<20} {high_emp[0]['Name']:<20} ₹{highest_salary}")
    print(f"{'Lowest':<20} {low_emp[0]['Name']:<20} ₹{lowest_salary}")
    print(f"{'Average':<20} All {emp_count}{' employees':<14} ₹{avg_salary:,.2f}")