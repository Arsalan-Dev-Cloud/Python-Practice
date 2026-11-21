import csv

file_path = "E:/Python-Practice/Day-22_CSV_Files_in_Python/CSV-Files/employees.csv"

try:
    with open(file_path, "r", newline = "", encoding = "utf-8-sig") as file:
        data = csv.DictReader(file)

        department = []
        salary_x = []
        total_salary = 0
        highest_salary = 0
        lowest_salary = 0
        emp_count = 0

        print("\nAvailable Departments:\n")

        for row in data:
            
            if row['Department'] not in department:
                
                department.append(row['Department'])

        for i in range(len(department)):
            
            print(i + 1, ".", department[i])

        dep_name = input("\nEnter Department: ")

        if dep_name.lower() not in [d.lower() for d in department]:
            
            print("Department Not Found!!!")
        
        else:
            
            file.seek(0)
            data = csv.DictReader(file)

            for row in data:
                
                if row['Department'].lower() == dep_name.lower():

                    salary_x.append(int(row['Salary']))
                    salary = int(row['Salary'])
                    total_salary += salary
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

            print()
            print("=" * 40)
            print(dep_name.upper(), "Department Salary Report")
            print("=" * 40)

            print(f"\n{'Total Employees':<20}: {emp_count}")
            print(f"{'Total Salary':<20}: {total_salary}")
            if emp_count > 0:
                print(f"{'Average Salary':<20}: {total_salary/emp_count}")
            else:
                print("No employee found in this department")
            print(f"{'Highest Salary':<20}: {highest_salary}")
            print(f"{'Lowest Salary':<20}: {lowest_salary}")
            print("=" * 40)

except FileNotFoundError:
    print("File not found!!!")