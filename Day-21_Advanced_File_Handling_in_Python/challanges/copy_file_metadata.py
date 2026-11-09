import shutil
import os

source_path = "E:/Python-Practice/Day-21_Advanced_File_Handling_in_Python/Files/Laptop.txt"

destination_path = "E:/Python-Practice/Day-21_Advanced_File_Handling_in_Python/Files/Laptop_Backup_Metadata.txt"

shutil.copy2(source_path, destination_path)

if os.path.exists(destination_path):
    print("File Copied Successfully With Metadata!")
    print("Metadata Backup Exists: True")
else:
    print("Metadata Backup Exists: False")


# Output:- 
"""
File Copied Successfully With Metadata!
Metadata Backup Exists: True
"""