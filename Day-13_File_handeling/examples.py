Data = {
    "Name": input("Enter the Name: "),
    "Course": input("Enter the Course: "),
    "City": input("Enter the City: ")
    }

with open("Data.txt", "w") as file:

    for key, value in Data.items():
        file.write(f"{key:<10}: {value}\n")

print("Data Saved Successfully.")