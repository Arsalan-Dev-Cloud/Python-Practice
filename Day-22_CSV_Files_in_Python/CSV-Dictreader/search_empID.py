import csv

file_path = "E:/Python-Practice/Day-22_CSV_Files_in_Python/CSV-Files/employees.csv"

emp_id = input("Enter Employee ID: ")

found = False

try:
    with open(file_path, "r", newline = "", encoding = "utf-8-sig") as file:
        data = csv.DictReader(file)

        for row in data:

            if row['Employee_ID'] == emp_id:

                print("\nEmployee Found!!!")
                print("-" * 35)
                print(f"{'Employee ID':<20}: {row['Employee_ID']}")
                print(f"{'Name':<20}: {row['Name']}")
                print(f"{'Department':<20}: {row['Department']}")
                print(f"{'Salary':<20}: {row['Salary']}")
                found = True
                break

        if not found:
            print("Employee Not Found!!!")
            
except FileNotFoundError:
    print("File Not Found!!!")