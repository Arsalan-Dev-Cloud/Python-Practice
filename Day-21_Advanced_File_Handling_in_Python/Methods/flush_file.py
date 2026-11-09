file_path = "E:/Python-Practice/Day-21_Advanced_File_Handling_in_Python/Files/Laptop.txt"

with open(file_path, "a") as file:
    file.write("Operating System: Windows 11\n")
    file.flush()
    print("Data Flushed Successfully!")


with open(file_path, "r") as file:
    print(file.read())


# Output:-

"""
Data Flushed Successfully!
Brand: ASUS
RAM: 16GB DDR5
GPU: RTX 5050
Storage: 1TB NVMe SSD
Operating System: Windows 11
Storage: 1TB NVMe SSD
Operating System: Windows 11
"""