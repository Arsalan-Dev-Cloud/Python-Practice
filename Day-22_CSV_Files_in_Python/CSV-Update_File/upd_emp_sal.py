import csv

file_path = "E:/Python-Practice/Day-22_CSV_Files_in_Python/CSV-Files/employees.csv"

emp_id = input("Enter Employee ID: ")
new_salary = input("Enter New Salary: ")

employees = []
found = False

with open(file_path, "r", newline="", encoding="utf-8-sig") as file:
    data = csv.DictReader(file)

    for row in data:
        
        if row['Employee_ID'] == emp_id:
            
            row['Salary'] = new_salary
            found = True

        employees.append(row)
        

if found:

    with open(file_path, "w", newline="", encoding="utf-8-sig") as file:

        writer = csv.DictWriter(file, fieldnames=employees[0].keys())

        writer.writeheader()
        writer.writerows(employees)

    print("Employee Salary Updated Successfully!")

else:

    print("Employee Not Found!!!")