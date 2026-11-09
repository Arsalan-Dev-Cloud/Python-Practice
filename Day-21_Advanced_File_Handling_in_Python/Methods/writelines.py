laptop_details = [
    "Brand: ASUS\n",
    "Processor: Intel Core i7-14650HX\n",
    "RAM: 16GB DDR5\n"
    "GPU: RTX 5050\n"
    "Storage: 1TB NVMe SSD\n"
]

with open("E:/Python-Practice/Day-21_Advanced_File_Handling_in_Python/Files/Laptop_Specifications.txt", "w") as file:
    file.writelines(laptop_details)

print("Laptop details saved successfully!\n")

with open("E:/Python-Practice/Day-21_Advanced_File_Handling_in_Python/Files/Laptop_Specifications.txt", "r") as file:
    print("----- Laptop Specifications -----")
    print(file.read())