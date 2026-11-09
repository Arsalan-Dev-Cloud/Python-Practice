import os

file_path = "E:/Python-Practice/Day-21_Advanced_File_Handling_in_Python/Files/Laptop_Specifications.txt"

print("----- File Information -----")
if os.path.exists(file_path):
    print("File Exists: True")
    if os.path.isfile(file_path):
        print("Is a File: True")
        print("File Size:", os.path.getsize(file_path), "Bytes")
    else:
        print("Is a File: False")
else:
    print("File Exists: False")



# Output:-

"""
----- File Information -----
File Exists: True
Is a File: True
File Size: 101 Bytes
"""