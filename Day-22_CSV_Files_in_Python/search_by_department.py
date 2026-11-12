import csv

file_path = "E:/Python-Practice/Day-22_CSV_Files_in_Python/employees.csv"

search_department = input("Enter Department: ")

found = False

total_department_salary = 0

try:
    with open(file_path, "r", newline="") as file:
        data = csv.reader(file)

        next(data)

        print("\nEmployees in", search_department, "Department")
        print("=" * 40)

        for row in data:
            if row[2].lower() == search_department.lower():
                print("\nEmployee ID: ", row[0])
                print("Name: ", row[1])
                print("Department: ", row[2])
                print("Salary: ", row[3])
                print()
                print("-" * 40)
                
                salary = int(row[3])
                total_department_salary += salary

                found = True    

    if found:
        print("\nTotal", search_department, "Department Salary:", total_department_salary)
    else:
        print("Department Not Found!!!")

except FileNotFoundError:
    print("File Not Found!!!")
