import csv

file_path = "E:/Python-Practice/Day-22_CSV_Files_in_Python/CSV-Files/employees.csv"

try:
    with open(file_path, "r", newline="", encoding="utf-8-sig") as file:
        data = csv.DictReader(file)

        department = []

        print("\nAvailable Departments:\n")

        for row in data:
            if row['Department'] not in department:
                department.append(row['Department'])

        for i in range(len(department)):
            print(i + 1, ".", department[i])

        dep_name = input("\nEnter Department: ")

        if dep_name.lower() not in [d.lower() for d in department]:

            print("Department Not found!!!")

        else:

            file.seek(0)

            data = csv.DictReader(file)

            print("=" * 40)
            print(dep_name, "Department Employees")
            print("=" * 40)

            total_count = 0

            for row in data:
                if row["Department"].lower() == dep_name.lower():
                    print(f"\n{'Employee ID':<20}: {row['Employee_ID']}")
                    print(f"{'Name':<20}: {row['Name']}")
                    print(f"{'Salary':<20}: {row['Salary']}")
                    print("-" * 40)
                    total_count += 1

            print("Total Employees: ", total_count)
except FileNotFoundError:
    print("File Not Found!!!")