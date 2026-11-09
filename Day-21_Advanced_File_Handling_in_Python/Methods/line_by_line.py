file_path = "E:/Python-Practice/Day-21_Advanced_File_Handling_in_Python/Files/Laptop.txt"

with open(file_path, "r") as file:
    for i, line in enumerate(file, start=1):
        print(f"Line {i}:", line, end="")