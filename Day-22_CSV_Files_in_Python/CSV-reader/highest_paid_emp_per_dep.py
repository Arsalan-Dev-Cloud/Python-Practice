import csv

file_path = "E:/Python-Practice/Day-22_CSV_Files_in_Python/CSV-Files/employees.csv"

department_name = input("Enter Department: ")

salary_x = []
employee_x = []
highest_employee = []
highest_salary = 0

try:
    with open(file_path, "r", newline="") as file:
        data = csv.reader(file)

        next(data)

        for row in data:
            if row[2].lower() == department_name.lower():
                salary_x.append(int(row[3]))
                employee_x.append(row.copy())

        for i in range(len(salary_x)):

            count = 0

            for j in range(len(salary_x)):
                    
                if salary_x[i] >= salary_x[j] and i != j:
                    count += 1

            if count == len(salary_x) - 1:
                highest_salary = salary_x[i]
                highest_employee = employee_x[i].copy()

        if len(salary_x) > 0:

            print()
            print("=" * 40)
            print("HIGHEST-PAID EMPLOYEE")
            print("=" * 40)

            print(f"\n{'Employee ID':<20}: {highest_employee[0]}")
            print(f"{'Name':<20}: {highest_employee[1]}")
            print(f"{'Department':<20}: {highest_employee[2]}")
            print(f"{'Salary':<20}: {highest_employee[3]}")
        
        else:
        
            print("Department Not Found!!!")

except FileNotFoundError:
    print("File Not Found!!!")