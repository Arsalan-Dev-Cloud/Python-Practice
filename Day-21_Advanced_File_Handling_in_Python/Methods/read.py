with open("E:/Python-Practice/Day-21_Advanced_File_Handling_in_Python/Files/Laptop.txt","r") as file:
    Laptop_data = file.read()

print("----- Laptop Details -----")
print(Laptop_data)


# Output:-

"""
----- Laptop Details -----
Brand: ASUS
RAM: 16GB DDR5
GPU: RTX 5050
Storage: 1TB NVMe SSD
Operating System: Windows 11
Storage: 1TB NVMe SSD
Operating System: Windows 11
"""