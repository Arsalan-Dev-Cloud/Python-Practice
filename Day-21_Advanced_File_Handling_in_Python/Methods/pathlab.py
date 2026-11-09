from pathlib import Path

file_path = Path("E:/Python-Practice/Day-21_Advanced_File_Handling_in_Python/Files/Laptop.txt")

print("Exists:", file_path.exists())
print("Is File:", file_path.is_file())
print("Is Directory:", file_path.is_dir())
print("File Name:", file_path.name)
print("Extension:", file_path.suffix)
print("Parent Folder:", file_path.parent)
print("File Size:", file_path.stat().st_size, "Bytes")


"""
Method                  Purpose
.exists()	            Checks whether a path exists
.is_file()	            Checks whether it is a file
.is_dir()	            Checks whether it is a directory
.name	                Returns the file or folder name
.suffix	                Returns the file extension
.parent	                Returns the parent directory
.stat().st_size	        Returns file size in bytes
"""

# Output:-

"""
Exists: True
Is File: True
Is Directory: False
File Name: Laptop.txt
Extension: .txt
Parent Folder: E:\Python-Practice\Day-21_Advanced_File_Handling_in_Python\Files
File Size: 150 Bytes
"""