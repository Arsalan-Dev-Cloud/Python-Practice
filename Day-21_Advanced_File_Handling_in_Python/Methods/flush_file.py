file_path = "E:/Python-Practice/Day-21_Advanced_File_Handling_in_Python/Files/Laptop.txt"

with open(file_path, "a") as file:
    file.write("Operating System: Windows 11\n")
    file.flush()
    print("Data Flushed Successfully!")


with open(file_path, "r") as file:
    print(file.read())