# Day 13 – File Handling 📁🐍

## 📌 What is File Handling?

File handling allows a Python program to **create, read, write, append, and manage files**.

Normally, data stored in variables disappears when a program ends.

Example:

```python
name = "Arsalan"
marks = 90
```

When the program stops, these variables are removed from memory.

If we save the data inside a file, it remains available even after the program closes.

Example:

```text
Student.txt
```

Contents:

```text
Name      : Arsalan
Roll No.  : 60
Course    : Big Data
Marks     : 90
```

---

# Opening a File

Python provides the `open()` function for working with files.

### Syntax

```python
file = open("filename.txt", "mode")
```

Example:

```python
file = open("Student.txt", "r")
```

Here:

* `Student.txt` → File name
* `"r"` → File mode

---

# File Modes

The most commonly used file modes are:

| Mode  | Meaning | Purpose                                     |
| ----- | ------- | ------------------------------------------- |
| `"r"` | Read    | Reads an existing file                      |
| `"w"` | Write   | Writes data and overwrites existing content |
| `"a"` | Append  | Adds data without deleting existing content |
| `"x"` | Create  | Creates a new file                          |

---

# Read Mode – `"r"`

Used to read an existing file.

```python
with open("Student.txt", "r") as file:
    print(file.read())
```

If the file does not exist, Python raises:

```text
FileNotFoundError
```

---

# Write Mode – `"w"`

Used to write data into a file.

```python
with open("Student.txt", "w") as file:
    file.write("Name: Arsalan")
```

If the file doesn't exist, Python creates it.

⚠️ If the file already contains data, `"w"` **deletes the old contents before writing new data**.

Example:

Before:

```text
Name: Arsalan
Course: Big Data
```

Code:

```python
with open("Student.txt", "w") as file:
    file.write("Python")
```

After:

```text
Python
```

---

# Append Mode – `"a"`

Append mode adds new information **without deleting existing data**.

```python
with open("Student.txt", "a") as file:
    file.write("\nCity: Latur")
```

Before:

```text
Name: Arsalan
Course: Big Data
```

After:

```text
Name: Arsalan
Course: Big Data
City: Latur
```

### Easy Way to Remember

```text
w → Write/Replace
a → Add
r → Read
x → Create
```

---

# Create Mode – `"x"`

Creates a new file.

```python
with open("example.txt", "x") as file:
    file.write("Hello Python")
```

If the file already exists, Python raises:

```text
FileExistsError
```

---

# `with open()`

Recommended way to work with files:

```python
with open("Student.txt", "r") as file:
    print(file.read())
```

Python automatically closes the file when the `with` block finishes.

Without `with`:

```python
file = open("Student.txt", "r")

print(file.read())

file.close()
```

Using `with open()` is cleaner and safer.

---

# `read()`

Reads the complete file.

```python
with open("Student.txt", "r") as file:
    data = file.read()
    print(data)
```

You can also specify how much to read:

```python
with open("Student.txt", "r") as file:
    print(file.read(5))
```

This reads up to 5 characters from the current file position.

---

# `readline()`

Reads one line at a time.

```python
with open("Student.txt", "r") as file:
    print(file.readline())
```

Calling it again reads the next line:

```python
with open("Student.txt", "r") as file:
    print(file.readline())
    print(file.readline())
```

---

# `readlines()`

Reads all lines and returns them as a list.

```python
with open("Student.txt", "r") as file:
    lines = file.readlines()

print(lines)
```

Example output:

```python
[
    "Name: Arsalan\n",
    "Course: Big Data\n",
    "Marks: 90\n"
]
```

---

# Looping Through a File

A file can also be read line by line using a loop.

```python
with open("Student.txt", "r") as file:
    for line in file:
        print(line, end="")
```

Using:

```python
end=""
```

prevents `print()` from adding an additional newline.

---

# `write()`

Writes a string into a file.

```python
with open("Student.txt", "w") as file:
    file.write("Name: Arsalan")
```

Multiple lines:

```python
with open("Student.txt", "w") as file:
    file.write("Name: Arsalan\n")
    file.write("Course: Big Data\n")
    file.write("Marks: 90")
```

---

# `writelines()`

Writes multiple strings into a file.

```python
data = [
    "Maths\n",
    "Science\n",
    "English\n"
]

with open("subjects.txt", "w") as file:
    file.writelines(data)
```

Important:

`writelines()` does **not automatically add new lines**.

Therefore:

```python
"\n"
```

must be added manually when required.

---

# `tell()`

`tell()` returns the current position of the file cursor.

```python
with open("Student.txt", "r") as file:
    print(file.tell())

    file.read(5)

    print(file.tell())
```

The cursor starts near the beginning and moves as data is read. In simple ASCII text, reading 5 characters commonly advances the position from `0` to `5`.

---

# `seek()`

`seek()` changes the file cursor position.

```python
with open("Student.txt", "r") as file:

    print(file.read(5))

    file.seek(0)

    print(file.read(5))
```

`seek(0)` moves the cursor back to the beginning.

---

# `readable()`

Checks whether the file supports reading.

```python
with open("Student.txt", "r") as file:
    print(file.readable())
```

Output:

```text
True
```

---

# `writable()`

Checks whether the file supports writing.

```python
with open("Student.txt", "w") as file:
    print(file.writable())
```

Output:

```text
True
```

---

# `close()`

If we open a file manually:

```python
file = open("Student.txt", "r")
```

we should close it:

```python
file.close()
```

When using:

```python
with open(...)
```

Python automatically closes the file.

---

# Using Dictionaries with Files

Dictionaries can be combined with file handling.

```python
student = {
    "Name": "Arsalan",
    "Roll No.": 60,
    "Course": "Big Data",
    "Marks": 90
}

with open("Student.txt", "w") as file:

    for key, value in student.items():
        file.write(f"{key:<10}: {value}\n")
```

Output inside `Student.txt`:

```text
Name      : Arsalan
Roll No.  : 60
Course    : Big Data
Marks     : 90
```

---

# Appending Multiple Student Records

```python
student = {
    "Name": input("Enter the Name : "),
    "Roll No.": input("Enter the Roll No : "),
    "Course": input("Enter the Course : "),
    "Marks": input("Enter the Marks : ")
}

with open("Student.txt", "a") as file:

    for key, value in student.items():
        file.write(f"{key:<10}: {value}\n")

    file.write("\n")
```

Running the program multiple times can produce:

```text
Name      : Arsalan
Roll No.  : 60
Course    : Big Data
Marks     : 90

Name      : Ali
Roll No.  : 61
Course    : Big Data
Marks     : 85
```

---

# Clearing File Contents

To delete everything inside a file while keeping the file:

```python
with open("Student.txt", "w") as file:
    pass
```

The file still exists, but its contents are removed.

---

# Deleting a File

Use the `os` module:

```python
import os

if os.path.exists("Student.txt"):
    os.remove("Student.txt")
    print("File deleted.")
else:
    print("File does not exist.")
```

⚠️ `os.remove()` deletes the actual file, not just its contents.

---

# Checking if a File Exists

```python
import os

if os.path.exists("Student.txt"):
    print("File exists.")
else:
    print("File does not exist.")
```

---

# Understanding File Paths

An important concept learned during this lesson was the **Current Working Directory**.

Suppose the terminal shows:

```text
PS E:\Python-Practice>
```

and the program is located at:

```text
E:\Python-Practice\Day-13_File_handeling\challange\write_file.py
```

If the program uses:

```python
open("Student.txt", "a")
```

Python normally resolves that relative path from the **current working directory**, not necessarily the folder containing the Python script.

This can cause Python to create:

```text
E:\Python-Practice\Student.txt
```

instead of using:

```text
E:\Python-Practice\Day-13_File_handeling\challange\Student.txt
```

---

# Solution 1 – Change Current Directory

Move into the program folder first:

```powershell
cd E:\Python-Practice\Day-13_File_handeling\challange
```

Then run:

```powershell
python write_file.py
```

Now the terminal should show:

```text
PS E:\Python-Practice\Day-13_File_handeling\challange>
```

---

# Solution 2 – Use `pathlib`

A more reliable solution is:

```python
from pathlib import Path

file_path = Path(__file__).parent / "Student.txt"

with open(file_path, "a") as file:
    file.write("Hello")
```

`Path(__file__).parent` refers to the directory containing the current Python script.

This makes the program work correctly even when it is launched from another directory.

---

# Important File Methods

| Method         | Purpose                              |
| -------------- | ------------------------------------ |
| `read()`       | Reads file contents                  |
| `readline()`   | Reads one line                       |
| `readlines()`  | Reads all lines into a list          |
| `write()`      | Writes one string                    |
| `writelines()` | Writes multiple strings              |
| `tell()`       | Returns current cursor position      |
| `seek()`       | Changes cursor position              |
| `readable()`   | Checks whether file supports reading |
| `writable()`   | Checks whether file supports writing |
| `close()`      | Closes the file                      |

---

# File Modes Summary

| Mode  | Read | Write |  Keeps Old Data  |
| ----- | :--: | :---: | :--------------: |
| `"r"` |   ✅  |   ❌   |         ✅        |
| `"w"` |   ❌  |   ✅   |         ❌        |
| `"a"` |   ❌  |   ✅   |         ✅        |
| `"x"` |   ❌  |   ✅   | Creates new file |

---

# Day 13 Challenge – Student Record System

The challenge was to create a Student Record File System.

Project structure:

```text
challange/
│
├── write_file.py
├── read_file.py
├── append_file.py
├── clear_file.py
└── Student.txt
```

### `write_file.py`

Creates/writes student information.

### `append_file.py`

Adds new student records without deleting previous records.

### `read_file.py`

Reads and displays all stored student records.

### `clear_file.py`

Clears all records while keeping `Student.txt`.

### `Student.txt`

Stores the student records permanently.

---

# Concepts Combined in the Challenge

The project combined concepts from previous lessons:

```text
User Input
    ↓
Dictionary
    ↓
for Loop
    ↓
f-String Formatting
    ↓
File Handling
    ↓
Student.txt
```

This demonstrates how different Python concepts can work together in one practical program.

---

# Important Points to Remember

* `"r"` reads a file.
* `"w"` writes but removes existing contents.
* `"a"` adds data without deleting old contents.
* `"x"` creates a new file.
* `with open()` automatically closes files.
* `\n` creates a new line.
* `readlines()` returns a list.
* `write()` accepts a string.
* `writelines()` can write multiple strings.
* `seek()` changes the cursor position.
* `tell()` reports the current cursor position.
* Relative file paths depend on the current working directory.
* `pathlib` can be used for more reliable file paths.

---

# Summary

In Day 13, you learned:

* File Handling
* Opening Files
* File Modes
* Reading Files
* Writing Files
* Appending Files
* Creating Files
* Clearing File Contents
* Deleting Files
* File Methods
* File Cursor Position
* Dictionaries with Files
* File Paths
* Current Working Directory
* `pathlib`
* Building a Student Record File System

File handling is extremely important in Python and is commonly used for:

* Data processing
* Automation
* Log files
* Configuration files
* Reports
* CSV processing
* Data Engineering pipelines

---

# Homework

1. Practice `read()`, `readline()`, and `readlines()`.
2. Practice `"w"` and `"a"` modes.
3. Practice `seek()` and `tell()`.
4. Add multiple students to `Student.txt`.
5. Read all saved records.
6. Clear the file using `clear_file.py`.
7. Practice working with relative file paths.
8. Push Day 13 to GitHub.

---

# Git Commit

```bash
git add .
git commit -m "Day 13 - File Handling Completed"
git push
```

---

# 🎯 Key Takeaway

> **File handling allows Python programs to store data permanently. Use `"r"` to read, `"w"` to replace/write, `"a"` to append, and `with open()` for safe and clean file operations.**
