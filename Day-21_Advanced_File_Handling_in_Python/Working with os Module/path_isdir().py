# Checking whether a folder exists

import os

file_path = "E:/Python-Practice/Day-21_Advanced_File_Handling_in_Python/Files/Laptop.txt"

if os.path.isdir(file_path):
    print("Folder exists!")
else:
    print("Folder does not exists!")