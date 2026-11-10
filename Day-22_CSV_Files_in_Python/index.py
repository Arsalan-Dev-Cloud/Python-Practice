import csv

file_path = "E:/Python-Practice/Day-22_CSV_Files_in_Python/employees.csv"

with open(file_path, "r", newline="") as file:

    data = list(csv.reader(file))

    for row_index, row in enumerate(data):

        print("Row Index:", row_index)

        for column_index, value in enumerate(row):

            print(f"Column {column_index}: {value}")

        print("-" * 40)


# Output:- 

"""
Row Index: 0
Column 0: Employee_ID
Column 1: Name
Column 2: Department
Column 3: Salary
----------------------------------------
Row Index: 1
Column 0: 101
Column 1: Arsalan
Column 2: IT
Column 3: 45000
----------------------------------------
Row Index: 2
Column 0: 102
Column 1: Rahul
Column 2: HR
Column 3: 35000
----------------------------------------
Row Index: 3
Column 0: 103
Column 1: Sameer
Column 2: Finance
Column 3: 40000
----------------------------------------
Row Index: 4
Column 0: 104
Column 1: Aditya
Column 2: Marketing
Column 3: 38000
----------------------------------------
Row Index: 5
Column 0: 105
Column 1: Ali
Column 2: IT
Column 3: 50000 
----------------------------------------
"""