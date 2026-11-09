import os
import shutil
from pathlib import Path


folder_path = "E:/Python-Practice/Day-21_Advanced_File_Handling_in_Python/Files"

print("=" * 75, "LAPTOP FILE MANAGER","=" * 75, "\n")

print("=" * 20, "DIRECTORY CONTENTS", "=" * 20, "\n")

try:
    items = os.listdir(folder_path)

    for item in items:

        item_path = os.path.join(folder_path, item)

        if os.path.isfile(item_path):
            print("File:", item)
        elif os.path.isdir(item_path):
            print("Folder:", item)
except FileNotFoundError:
    print("Error: Directory Not Found!")
 
except PermissionError:
    print("Error: Permission Denied!")

except OSError as error:
    print("Directory Operation Failed:", error)

print()
print("=" * 150, "\n")

print("1. Display File Information")
print("2. Display Content")
print("3. Create Backup")
print("4. Move File")

try:
    Num = int(input("\nEnter the Number To select Process: "))

except ValueError:
    Num = 0

print()
print("=" * 150, "\n")


if Num == 1:

    try:
        file_name = input("Enter File Name to Display it's Information: ")

        file_path = Path(folder_path) / file_name

        if file_path.exists() and file_path.is_file():
            print("\n========== FILE INFORMATION ==========")
            print(f"{'File Name':<20}: {file_name}")
            print(f"{'File Extension':<20}: {file_path.suffix}")
            print(f"{'File Size':<20}: {file_path.stat().st_size} {'Bytes'}")
            print(f"{'Parent Folder':<20}: {file_path.parent}")
        else:
            print("File not Found!!!")

    except PermissionError:
        print("Error: Permission Denied!")

    except OSError as error:
        print("File Information Error:", error)

    print()
    print("=" * 150, "\n")

elif Num == 2:

    try:
        file_name = input("Enter File Name to Read the Content: ")

        file_path = Path(folder_path) / file_name

        if file_path.exists() and file_path.is_file():
            if file_path.suffix.lower() != ".txt":
                print("Only Text Files Are Supported!")
            else:
                print("\n========== FILE CONTENT ==========")
                with open(file_path, "r", encoding="utf-8") as file:
                    print(file.read())
        else:
            print("File not Found!!!")

    except FileNotFoundError:
        print("Error: File not Found!")

    except PermissionError:
        print("Permission Denied!")

    except UnicodeDecodeError:
        print("Error: Unable to Decode File Content!")

    except OSError as error:
        print("File Reading Error:", error)

    print()
    print("=" * 150, "\n")

elif Num == 3:

    try:
        file_name = input("Enter File Name to Create Backup: ")

        source_path = Path(folder_path) / file_name
        backup_name = f"{source_path.stem}_Backup{source_path.suffix}"
        destination_path = Path(folder_path) / backup_name

        if source_path.exists() and source_path.is_file():
            
            if destination_path.exists():
                print("Backup Already Exists!!!")
            else:
                shutil.copy2(source_path, destination_path)        
                print("\n========== BACKUP INFORMATION ==========")
                print("Original File:", file_name)
                print("Backup File:", backup_name)
                print("Backup Created Successfully:", destination_path.exists())
        else:
            print("File Not Found!!!")

    except FileNotFoundError:
        print("Error: Source File or Destination Not Found!")

    except PermissionError:
        print("Error: Permission Denied!")

    except shutil.SameFileError:
        print("Error: Source and Destination Are the Same File!")

    except shutil.Error as error:
        print("Backup Operation Failed:", error)

    except OSError as error:
        print("File System Error:", error)

    print()
    print("=" * 150, "\n")

elif Num == 4:

    try:
        file_name = input("Enter File Name to Move: ")

        source_path = Path(folder_path) / file_name
        destination_folder = Path("E:/Python-Practice/Day-21_Advanced_File_Handling_in_Python/Practice") / file_name
        destination_folder.parent.mkdir(parents=True, exist_ok=True)

        if source_path.exists() and source_path.is_file():

            if destination_folder.exists():
                print("File Already Present!!!")
            else:
                shutil.move(source_path, destination_folder)
                print("\n========== MOVE FILE INFORMATION ==========")
                print("File Moved Successfully!")
                print("Original Location Exists:", source_path.exists())
                print("New Location Exists:", destination_folder.exists())
        else:
            print("File Not Found!!!")

    except FileNotFoundError:
        print("Error: Source File or Destination Folder not Found!")

    except PermissionError:
        print("Error: Permission Denied!")

    except shutil.Error as error:
        print("Move Operation Failed:", error)

    except OSError as error:
        print("File System Error:", error)

    print()
    print("=" * 150, "\n")

else:
    print("Invalid Input!!!!")