# Day 21 – Advanced File Handling in Python

## 1. Introduction

File handling allows Python programs to create, read, write, append, modify, copy, move, and delete files.

Python provides built-in file handling functions and modules such as:

- `open()`
- `os`
- `pathlib`
- `shutil`

These tools help us manage files and directories efficiently.

---

## 2. Writing Files – `open()` with `"w"`

The `"w"` mode is used to create a new file or overwrite an existing file.

### Syntax

```python
with open("Laptop.txt", "w") as file:
    file.write("Brand: ASUS")
```

### Explanation

- `open()` opens or creates a file.
- `"w"` represents write mode.
- `write()` writes content into the file.
- `with` automatically closes the file after the operation.

### Output

```text
A file named Laptop.txt is created.
```

### Important Point

If the file already exists, `"w"` overwrites its previous content.

---

## 3. Reading Files – `open()` with `"r"`

The `"r"` mode is used to read the contents of an existing file.

### Syntax

```python
with open("Laptop.txt", "r") as file:
    content = file.read()

print(content)
```

### Output

```text
Brand: ASUS
RAM: 16GB DDR5
GPU: RTX 5050
Storage: 1TB NVMe SSD
Operating System: Windows 11
```

### Important Point

If the file doesn't exist, Python raises `FileNotFoundError`.

---

## 4. Appending Files – `open()` with `"a"`

The `"a"` mode adds new content to the end of an existing file without deleting its previous content.

### Syntax

```python
with open("Laptop.txt", "a") as file:
    file.write("\nProcessor: Intel Core i7-14650HX")
```

### Important Point

- `"a"` preserves existing content.
- If the file doesn't exist, Python creates it.
- `\n` adds a new line.

---

## 5. Reading Files Line by Line

We can use a `for` loop to read a file one line at a time.

### Example 1 – Using a for loop

```python
with open("Laptop.txt", "r") as file:
    for line in file:
        print(line, end="")
```

### Example 2 – Using enumerate()

```python
with open("Laptop.txt", "r") as file:
    for line_number, line in enumerate(file, start=1):
        print(line_number, line, end="")
```

### Output

```text
1 Brand: ASUS
2 RAM: 16GB DDR5
3 GPU: RTX 5050
4 Storage: 1TB NVMe SSD
5 Operating System: Windows 11
```

### Important Point

`end=""` prevents `print()` from adding an additional newline when the line already contains one.

---

## 6. Exception Handling in File Operations

Exception handling prevents a program from crashing when an error occurs.

### Syntax

```python
try:
    # Code that might produce an error

except FileNotFoundError:
    print("File Not Found!")

except PermissionError:
    print("Permission Denied!")
```

### Common File Exceptions

| Exception | Meaning |
|---|---|
| FileNotFoundError | File doesn't exist |
| PermissionError | Access is denied |
| IsADirectoryError | A directory was used where a file was expected |
| UnicodeDecodeError | Text decoding failed |
| OSError | General operating-system-related error |

### Example

```python
try:
    with open("Laptop.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File Not Found!")

except PermissionError:
    print("Permission Denied!")

except OSError as error:
    print("File Operation Error:", error)
```

### Important Points

- `try` contains potentially risky code.
- `except` handles errors.
- `as error` stores the exception details.
- Specific exceptions should be caught before general exceptions.

---

## 7. Reading with `readline()` and `readlines()`

Python provides two additional methods for reading file content.

### readline()

Reads one line at a time.

```python
with open("Laptop.txt", "r") as file:
    print(file.readline())
    print(file.readline())
```

### Output

```text
Brand: ASUS

RAM: 16GB DDR5
```

### readlines()

Reads all lines and returns them as a list.

```python
with open("Laptop.txt", "r") as file:
    lines = file.readlines()

print(lines)
```

### Output

```python
[
    'Brand: ASUS\n',
    'RAM: 16GB DDR5\n',
    'GPU: RTX 5050\n'
]
```

### Difference

| Method | Description |
|---|---|
| read() | Reads the entire file as a string |
| readline() | Reads one line |
| readlines() | Reads all lines into a list |

---

## 8. File Pointer – `tell()` and `seek()`

Python maintains a file pointer that tracks the current reading or writing position.

### tell()

Returns the current file position.

```python
with open("Laptop.txt", "r") as file:
    print(file.tell())

    file.read(5)

    print(file.tell())
```

### Output

```text
0
5
```

### seek()

Moves the file pointer to a specified position.

```python
with open("Laptop.txt", "r") as file:
    print(file.read(5))

    file.seek(0)

    print(file.read(5))
```

### Output

```text
Brand
Brand
```

### Important Point

`seek(0)` moves the pointer back to the beginning of the file.

In text mode, file positions are not always equivalent to character counts, especially with multibyte encodings.

---

## 9. Flushing File Data – `flush()`

Python uses buffering to temporarily hold data before writing it to the underlying file.

The `flush()` method sends buffered data to the underlying file object.

### Example

```python
with open("Laptop.txt", "w") as file:
    file.write("Brand: ASUS")

    file.flush()

    print("Data Flushed Successfully!")
```

### Output

```text
Data Flushed Successfully!
```

### Important Point

`flush()` does not guarantee that data has been physically written to storage.

Using `with open()` automatically closes the file and flushes remaining buffered data.

---

## 10. Writing Multiple Lines – `writelines()`

The `writelines()` method writes multiple strings into a file.

### Example

```python
laptop_details = [
    "Brand: ASUS\n",
    "RAM: 16GB DDR5\n",
    "GPU: RTX 5050\n",
    "Storage: 1TB NVMe SSD\n"
]

with open("Laptop.txt", "w") as file:
    file.writelines(laptop_details)
```

### Important Point

`writelines()` does not automatically add newline characters.

We must include `\n` ourselves.

---

## 11. OS Module – File and Directory Management

The `os` module provides functions to interact with the operating system.

### Import

```python
import os
```

### Important Functions

| Function | Purpose |
|---|---|
| os.path.exists() | Checks whether a path exists |
| os.path.isfile() | Checks whether a path is a file |
| os.path.isdir() | Checks whether a path is a directory |
| os.path.getsize() | Returns file size in bytes |
| os.listdir() | Lists directory contents |
| os.mkdir() | Creates a directory |
| os.makedirs() | Creates nested directories |
| os.remove() | Deletes a file |
| os.rmdir() | Removes an empty directory |

### Example

```python
import os

folder_path = "E:/Python-Practice/Day-21_Advanced_File_Handling_in_Python/Files"

if os.path.exists(folder_path):
    print("Directory Exists!")

if os.path.isdir(folder_path):
    print("This is a Directory!")
```

### Creating a directory

```python
os.mkdir("Practice")
```

### Deleting a file

```python
os.remove("test.txt")
```

**Warning:** `os.remove()` permanently deletes a file. Verify the path before using it.

---

## 12. Creating Nested Directories – `os.makedirs()`

The `os.makedirs()` function creates multiple directories, including parent directories.

### Example

```python
import os

folder_path = "E:/Python-Practice/Day-21/Practice/Python/File_Handling"

os.makedirs(folder_path, exist_ok=True)

print("Folders Created Successfully!")
```

### Output

```text
Folders Created Successfully!
```

### Important Point

`exist_ok=True` prevents an error if the directory already exists.

---

## 13. Listing Directory Contents – `os.listdir()`

The `os.listdir()` function returns the names of files and directories inside a given directory.

### Example

```python
import os

folder_path = "E:/Python-Practice/Day-21_Advanced_File_Handling_in_Python/Files"

items = os.listdir(folder_path)

for item in items:

    item_path = os.path.join(folder_path, item)

    if os.path.isfile(item_path):
        print("File:", item)

    elif os.path.isdir(item_path):
        print("Folder:", item)
```

### Output

```text
File: Laptop.txt
File: Laptop_Backup.txt
File: Laptop_Specifications.txt
File: testx.txt
```

### Important Point

`os.path.join()` safely combines directory and file names.

---

## 14. Recursive Directory Traversal – `os.walk()`

The `os.walk()` function traverses a directory and all its subdirectories.

### Syntax

```python
os.walk(folder_path)
```

It provides three values:

- `root`: Current directory path.
- `dirs`: List of subdirectories.
- `files`: List of files.

### Example

```python
import os

folder_path = "E:/Python-Practice/Day-21_Advanced_File_Handling_in_Python"

for root, dirs, files in os.walk(folder_path):

    print("\nCurrent Directory:", root)

    print("Folders:", dirs)

    print("Files:", files)
```

### Important Point

Unlike `os.listdir()`, `os.walk()` explores nested directories recursively.

---

## 15. Pathlib Module – Modern Path Handling

The `pathlib` module provides an object-oriented approach to working with filesystem paths.

### Import

```python
from pathlib import Path
```

### Creating a path

```python
file_path = Path("E:/Python-Practice/Day-21/Laptop.txt")
```

### Important Methods and Attributes

| Method / Attribute | Purpose |
|---|---|
| exists() | Checks whether path exists |
| is_file() | Checks whether path is a file |
| is_dir() | Checks whether path is a directory |
| name | Returns filename |
| suffix | Returns file extension |
| parent | Returns parent directory |
| stat().st_size | Returns file size |
| mkdir() | Creates directory |
| unlink() | Deletes a file |

### Example

```python
from pathlib import Path

file_path = Path("E:/Python-Practice/Day-21/Laptop.txt")

if file_path.exists() and file_path.is_file():

    print("File Name:", file_path.name)
    print("Extension:", file_path.suffix)
    print("Parent Folder:", file_path.parent)
    print("File Size:", file_path.stat().st_size)
```

### Joining Paths

```python
folder_path = Path("E:/Python-Practice/Day-21/Files")

file_path = folder_path / "Laptop.txt"

print(file_path)
```

### Important Point

`pathlib` makes filesystem path operations cleaner and more readable than manually concatenating strings.

---

## 16. Shutil Module – Copying and Moving Files

The `shutil` module provides high-level file operations.

### Import

```python
import shutil
```

### copy()

Copies a file's contents and permission mode.

```python
shutil.copy("Laptop.txt", "Laptop_Backup.txt")
```

### copy2()

Copies a file and attempts to preserve additional metadata, such as modification times.

```python
shutil.copy2("Laptop.txt", "Laptop_Backup.txt")
```

### move()

Moves a file from one location to another.

```python
shutil.move("Laptop.txt", "Practice/Laptop.txt")
```

### Difference

| Function | Purpose |
|---|---|
| copy() | Copies file content and permission mode |
| copy2() | Copies content and attempts to preserve additional metadata |
| move() | Moves a file to another location |

### Important Point

`shutil.move()` removes the original file from its original location after a successful move.

---

# 17. Mini Project – Laptop File Manager

## Project Overview

The Laptop File Manager is a command-line application developed using Python's file-handling capabilities.

It allows users to manage files and directories through a simple menu-driven interface.

### Project Location

```text
E:\Python-Practice\Day-21_Advanced_File_Handling_in_Python
```

### Project Structure

```text
Day-21_Advanced_File_Handling_in_Python/
│
├── Files/
│   ├── Laptop.txt
│   ├── Laptop_Specifications.txt
│   └── Other test files
│
├── Practice/
│
├── laptop_file_manager.py
│
└── notes.md
```

## Project Features

1. Display files and folders.
2. Display file information.
3. Read text file contents.
4. Create file backups.
5. Move files.
6. Handle exceptions.

## Modules Used

```python
import os
import shutil
from pathlib import Path
```

| Module | Usage |
|---|---|
| os | Directory listing and path operations |
| shutil | Copying and moving files |
| pathlib | Modern path handling |

## Exception Handling Used

The project handles:

```python
FileNotFoundError
PermissionError
UnicodeDecodeError
shutil.SameFileError
shutil.Error
OSError
ValueError
```

The program uses specific exceptions before general exceptions wherever appropriate.

## Important Project Concepts

### 1. Menu-driven programming

The user selects an operation using a numeric menu.

```python
if Num == 1:
    print("Display File Information")

elif Num == 2:
    print("Read File Content")

elif Num == 3:
    print("Create Backup")

elif Num == 4:
    print("Move File")

else:
    print("Invalid Input!")
```

### 2. File backup

```python
backup_name = f"{source_path.stem}_Backup{source_path.suffix}"

destination_path = Path(folder_path) / backup_name

if destination_path.exists():
    print("Backup Already Exists!")

else:
    shutil.copy2(source_path, destination_path)
```

### 3. File movement

```python
shutil.move(source_path, destination_folder)
```

### 4. Exception handling

```python
try:
    # File operation

except FileNotFoundError:
    print("File Not Found!")

except PermissionError:
    print("Permission Denied!")

except OSError as error:
    print("File Operation Error:", error)
```

---

# 18. Important Differences – Quick Revision

| Concept | Description |
|---|---|
| `"r"` | Read |
| `"w"` | Write / overwrite |
| `"a"` | Append |
| `read()` | Read entire file |
| `readline()` | Read one line |
| `readlines()` | Read all lines into a list |
| `write()` | Write a string |
| `writelines()` | Write multiple strings |
| `tell()` | Get file pointer position |
| `seek()` | Change file pointer position |
| `flush()` | Flush buffered data |
| `os.listdir()` | List directory contents |
| `os.walk()` | Traverse directories recursively |
| `Path()` | Create a path object |
| `shutil.copy2()` | Copy file with additional metadata |
| `shutil.move()` | Move file |

---

# 19. What I Learned on Day 21

After completing Day 21, I can:

- Create, read, write and append files.
- Read files line by line.
- Handle file-related exceptions.
- Work with file pointers.
- Flush buffered data.
- Write multiple lines using `writelines()`.
- Create, delete and inspect directories.
- Traverse directories recursively.
- Manage filesystem paths using `pathlib`.
- Copy and move files using `shutil`.
- Build a menu-driven file management application.
- Apply exception handling to real-world file operations.

---

# Day 21 – Completed

**Topic:** Advanced File Handling in Python

**Concepts Completed:** 15/15

**Mini Project:** Laptop File Manager

**Status:** Completed

**Next:** Day 22 – Advanced Python Concepts

