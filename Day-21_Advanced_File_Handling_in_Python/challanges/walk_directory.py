import os

folder_path = "E:/Python-Practice/Day-21_Advanced_File_Handling_in_Python"

print("=" * 50, "DIRECTORY TREE", "=" * 50)

for root, dirs, files in os.walk(folder_path):

    print("\nCurrent Directory:", root)
    print("Folders:", dirs)
    print("Files:", files)
    print("-" * 100)