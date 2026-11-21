import csv

file_path = "E:/Python-Practice/Day-22_CSV_Files_in_Python/CSV-Files/employees.csv"

with open(file_path, "r", newline="", encoding="utf-8-sig") as file:
    data = csv.DictReader(file)

    print("=" * 40)
    print("Employee Information")
    print("=" * 40)
    count = 0

    for row in data:
        count += 1
        print(f"\n{'Employee ID':<20}: {row['Employee_ID']}")
        print(f"{'Name':<20}: {row['Name']}")
        print(f"{'Department':<20}: {row['Department']}")
        print(f"{'Salary':<20} {row['Salary']}")
        print("-" * 40)

    print("Total Employees: ", count)