# Deleting a file

import os

file_path = "E:/Python-Practice/Day-21_Advanced_File_Handling_in_Python/Files/testx.txt"

if os.path.exists(file_path):
    os.remove(file_path)
    print("File deleted successfully!")
else:
    print("File does not exist!")


# Important: os.remove() permanently removes the specified file. Always check the path before deleting. 
# Don't run this example against your actual laptop specification files.