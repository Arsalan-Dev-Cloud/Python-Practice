import os

folders_path = "E:/Python-Practice/Day-21_Advanced_File_Handling_in_Python/Practice/Python/File_Handling/"

os.makedirs(folders_path, exist_ok=True)

print("Folders Created Successfully!")

if os.path.isdir(folders_path):
    print("Directory Exists: True")
else:
    print("Directory Exists: False")



# Output:- 
"""
Directory Exists: True
Folders Created Successfully!
"""