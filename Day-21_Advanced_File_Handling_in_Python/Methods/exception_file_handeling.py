try:
    with open("E:/Python-Practice/Day-21_Advanced_File_Handling_in_Python/Files/Latop.txt", "r") as file:
        data = file.read()

    print(data)

except FileNotFoundError:
    print("Error: File Not FOUND !!!")


# Output:-

"""
Error: File Not FOUND !!!
"""