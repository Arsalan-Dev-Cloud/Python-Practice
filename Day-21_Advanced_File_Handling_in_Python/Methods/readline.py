with open("E:/Python-Practice/Day-21_Advanced_File_Handling_in_Python/Files/Laptop.txt", "r") as file:
    Laptop_data = file.readlines()

    print("--------- Laptop Data ----------")
    print(Laptop_data)
    print("Total Lines =", len(Laptop_data))