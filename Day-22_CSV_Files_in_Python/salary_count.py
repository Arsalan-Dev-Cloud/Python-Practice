import csv

file_path = "E:/Python-Practice/Day-22_CSV_Files_in_Python/employees.csv"

with open(file_path, "r", newline="") as file:
    data = csv.reader(file)

    next(data)

    total_salary = 0
    
    for row in data:

        salary = int(row[3])

        total_salary += salary

print("Total Salary:", total_salary)