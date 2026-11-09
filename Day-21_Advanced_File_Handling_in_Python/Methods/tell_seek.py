with open("E:/Python-Practice/Day-21_Advanced_File_Handling_in_Python/Files/Laptop.txt", "r") as file:

    print("Initial Position: ", file.tell())
    print("First Read:", file.read(5))
    print("Current Position:", file.tell())
    file.seek(0)
    print("After Seek(0):", file.tell())
    print("Second Read:", file.read(5))