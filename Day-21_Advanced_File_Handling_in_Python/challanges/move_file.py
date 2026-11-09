import shutil
import os

source_path = "E:/Python-Practice/Day-21_Advanced_File_Handling_in_Python/Files/Laptop_Backup_Metadata.txt"

destination_path = "E:/Python-Practice/Day-21_Advanced_File_Handling_in_Python/Practice/Laptop_Backup_Metadata.txt"

shutil.move(source_path, destination_path)

print("File Moved Successfully!")
print("Original File Exists:", os.path.exists(source_path))
print("Moved File Exists:", os.path.exists(destination_path))