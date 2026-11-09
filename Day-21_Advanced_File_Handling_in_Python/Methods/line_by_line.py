file_path = "E:/Python-Practice/Day-21_Advanced_File_Handling_in_Python/Files/Laptop.txt"

with open(file_path, "r") as file:
    for i, line in enumerate(file, start=1):
        print(f"Line {i}:", line, end="")


# Output:-

"""
Line 1: Brand: ASUS
Line 2: RAM: 16GB DDR5
Line 3: GPU: RTX 5050
Line 4: Storage: 1TB NVMe SSD
Line 5: Operating System: Windows 11
Line 6: Storage: 1TB NVMe SSD
Line 7: Operating System: Windows 11
"""