import os

folder_path = "E:/Python-Practice/Day-21_Advanced_File_Handling_in_Python"

items = os.listdir(folder_path)

print("----- Directory Contents -----")

for item in items:

    item_path = os.path.join(folder_path, item)

    if os.path.isfile(item_path):
        print("Files:", item)

    if os.path.isdir(item_path):
        print("Folder:", item)


# Output:-

"""
----- Directory Contents -----
Folder: challanges
Folder: Files
Files: laptop_file_manager.py
Folder: Methods
Files: notes.md
Folder: Practice
Folder: Working with os Module
"""