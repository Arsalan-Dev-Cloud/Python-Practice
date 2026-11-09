with open("E:/Python-Practice/Day-21_Advanced_File_Handling_in_Python/Files/Laptop.txt", "r") as file:
    Laptop_data = file.readlines()

    print("--------- Laptop Data ----------")
    print(Laptop_data)
    print("Total Lines =", len(Laptop_data))


# Output:-

"""
--------- Laptop Data ----------
['Brand: ASUS\n', 'RAM: 16GB DDR5\n', 'GPU: RTX 5050\n', 'Storage: 1TB NVMe SSD\n', 'Operating System: Windows 11\n', 'Storage: 1TB NVMe SSD\n', 'Operating System: Windows 11\n']
Total Lines = 7
"""