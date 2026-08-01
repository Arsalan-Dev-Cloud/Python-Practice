# -------- Day 13 - File Methods --------

with open("student.txt", "r") as file:

    print("Readable :", file.readable())
    print("Writable :", file.writable())

    print("\nCurrent Position :", file.tell())

    print("\nFirst 5 Characters:")
    print(file.read(5))

    print("\nPosition After Reading :", file.tell())

    file.seek(0)

    print("\nPosition After seek(0) :", file.tell())

    print("\nComplete File:")
    print(file.read())