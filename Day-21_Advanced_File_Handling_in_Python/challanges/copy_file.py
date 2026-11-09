import shutil
import os

source_path = "E:/Python-Practice/Day-21_Advanced_File_Handling_in_Python/Files/Laptop.txt"

destination_path = "E:/Python-Practice/Day-21_Advanced_File_Handling_in_Python/Files/Laptop_Backup.txt"

shutil.copy(source_path, destination_path)


if os.path.exists(destination_path):
    print("File Copied Successfully!!!")
    print("Backup File Exists: True")
else:
    print("Backup File Exists: False")


# Output:-
"""
File Copied Successfully!!!
Backup File Exists: True
"""