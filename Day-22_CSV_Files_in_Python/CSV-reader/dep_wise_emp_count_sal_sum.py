import csv

file_path = "E:/Python-Practice/Day-22_CSV_Files_in_Python/CSV-Files/employees.csv"

department = []
employee_x = []
salary_x = []

highest_salary = 0
lowest_salary = 0
total_salary = 0

try:
    with open(file_path, "r", newline="") as file:
        Data = csv.reader(file)
        next(Data)

        # All Department Appending
        print("\nAvailable Departments:\n")

        for row in Data:
            if row[2] not in department:
                department.append(row[2])

        for i in range(len(department)):
            print(i + 1, ".", department[i])

        # Department Name Entering
        Dep_name = input("\nEnter Department: ")

        file.seek(0)

        Data = csv.reader(file)
        next(Data)

        for row in Data:
            if row[2].lower() == Dep_name.lower():
                employee_x.append(row.copy())

        if len(employee_x) == 0:
            print("Department Not Found!!!")
        else:
            # Total and Average Salary Count
            for i in range(len(employee_x)):
            
                salary_x.append(int(employee_x[i][3]))
                        
                salary = salary_x[i]
                        
                total_salary += salary
            
            Avg_salary = total_salary / len(employee_x)           
        

            # Highest & Lowest Salary Count
            for k in range(len(employee_x)):
                high_count = 0
                lowe_count = 0
                for l in range(len(employee_x)):

                    if salary_x[k] >= salary_x[l] and k != l:
                        high_count += 1

                    if salary_x[k] <= salary_x[l] and k != l:
                        lowe_count += 1

                if high_count == len(salary_x) - 1:
                    highest_salary = salary_x[k]

                if lowe_count == len(salary_x) - 1:
                    lowest_salary = salary_x[k]

            # Displaying Details of Department
            print()
            print("=" * 40)
            print("       DEPARTMENT SALARY SUMMARY")
            print("=" * 40)
            print()

            print(f"{'Department':<20}: {Dep_name.upper()}")
            print(f"{'Total Employees':<20}: {len(employee_x)}")
            print(f"{'Total Salary':<20}: {total_salary}")
            print(f"{'Average Salary':<20}: {Avg_salary}")
            print(f"{'Highest Salary':<20}: {highest_salary}")
            print(f"{'Lowest Salary':<20}: {lowest_salary}")

except FileNotFoundError:
    print("File Not Found!!!")