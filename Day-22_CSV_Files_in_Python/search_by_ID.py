import csv

file_path = "E:/Python-Practice/Day-22_CSV_Files_in_Python/employees.csv"

search_ID = input("Enter the ID to search: ")

found = False

try:
    with open(file_path, "r", newline="") as file:
        
        data = csv.reader(file)
        next(data)
    
        for row in data:
            if row[0] == search_ID:
                print("\nEmployee Found!!!")
                print("Employee ID: ", row[0])
                print("Name: ", row[1])
                print("Department: ", row[2])
                print("Salary: ", row[3])

                found = True
                break

    if found == False:
        print("\nEmployee Not Found!!!")
    
except FileNotFoundError:
        print("File Not Found!!!") 