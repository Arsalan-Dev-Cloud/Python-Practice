from pathlib import Path

file_path = Path("E:/Python-Practice/Day-21_Advanced_File_Handling_in_Python/Files/Laptop.txt")

if file_path.exists():
    print("File Exists!")
    if file_path.is_file():
        print("Is File: True")
    else:
        print("Is File: False")

    print("File Name:", file_path.name)
    print("File Extension:", file_path.suffix)
    print("Parent Folder:", file_path.parent)
    print("File Size:", file_path.stat().st_size, "Bytes")
    print("Is Directory:", file_path.is_dir())
else:
    print("File does not exists!!")