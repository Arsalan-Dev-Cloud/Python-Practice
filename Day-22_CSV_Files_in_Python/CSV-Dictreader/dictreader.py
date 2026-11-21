import csv

file_path = "E:/Python-Practice/Day-22_CSV_Files_in_Python/CSV-Files/employees.csv"

with open(file_path, "r", newline="") as file:

    Data = csv.DictReader(file)

    for row in Data:
        print(row)