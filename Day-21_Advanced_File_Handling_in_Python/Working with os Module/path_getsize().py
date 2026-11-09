# Getting file information -- Size

import os

file_path = "E:/Python-Practice/Day-21_Advanced_File_Handling_in_Python/Files/Laptop.txt"

if os.path.exists(file_path):
    size = os.path.getsize(file_path)
    print("File Size:", size, "Bytes")
else:
    print("Files not found!")