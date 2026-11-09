# To check whether File exists or not

import os

file_path = "E:/Python-Practice/Day-21_Advanced_File_Handling_in_Python/Files/Laptop.txt"

if os.path.exists(file_path):
    print("File exists!")
else:
    print("File does not exist!")