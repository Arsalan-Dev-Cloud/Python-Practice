import os

folder_path = "E:/Python-Practice/Day-21_Advanced_File_Handling_in_Python"

print("=" * 50, "DIRECTORY TREE", "=" * 50)

for root, dirs, files in os.walk(folder_path):

    print("\nCurrent Directory:", root)
    print("Folders:", dirs)
    print("Files:", files)
    print("-" * 100)



# Output:-

"""
================================================== DIRECTORY TREE ==================================================

Current Directory: E:/Python-Practice/Day-21_Advanced_File_Handling_in_Python
Folders: ['challanges', 'Files', 'Methods', 'Practice', 'Working with os Module']
Files: ['laptop_file_manager.py', 'notes.md']
----------------------------------------------------------------------------------------------------

Current Directory: E:/Python-Practice/Day-21_Advanced_File_Handling_in_Python\challanges
Folders: []
Files: ['copy_file.py', 'copy_file_metadata.py', 'create_directories.py', 'list_directory.py', 'move_file.py', 'os_module.py', 'pathlib_practice.py', 'walk_directory.py']
----------------------------------------------------------------------------------------------------

Current Directory: E:/Python-Practice/Day-21_Advanced_File_Handling_in_Python\Files
Folders: []
Files: ['Laptop.txt', 'Laptop_Backup.txt', 'Laptop_Specifications.txt', 'testx.txt']
----------------------------------------------------------------------------------------------------

Current Directory: E:/Python-Practice/Day-21_Advanced_File_Handling_in_Python\Methods
Folders: []
Files: ['append.py', 'exception_file_handeling.py', 'flush_file.py', 'line_by_line.py', 'pathlab.py', 'read.py', 'readline.py', 'tell_seek.py', 'write.py', 'writelines.py']
----------------------------------------------------------------------------------------------------

Current Directory: E:/Python-Practice/Day-21_Advanced_File_Handling_in_Python\Practice
Folders: ['Python']
Files: ['Laptop_Backup_Metadata.txt', 'testx_Backup.txt']
----------------------------------------------------------------------------------------------------

Current Directory: E:/Python-Practice/Day-21_Advanced_File_Handling_in_Python\Practice\Python
Folders: ['File_Handling']
Files: []
----------------------------------------------------------------------------------------------------

Current Directory: E:/Python-Practice/Day-21_Advanced_File_Handling_in_Python\Practice\Python\File_Handling
Folders: []
Files: []
----------------------------------------------------------------------------------------------------

Current Directory: E:/Python-Practice/Day-21_Advanced_File_Handling_in_Python\Working with os Module
Folders: []
Files: ['os_remove().py', 'path_exists().py', 'path_getsize().py', 'path_isdir().py']
----------------------------------------------------------------------------------------------------
"""