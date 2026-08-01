#--------File methods in python-----------------

# read() - Reads the whole file

with open("student.txt", "r") as file:
    print(file.read())

# Another way to read the file:
with open("student.txt", "r") as file:
    print(file.read(5))

# readline() - Reads a single line from the file

with open("student.txt", "r") as file:
    print(file.readline())
    print(file.readline())

# readlines() - Reads all the lines of a file and returns them as a list

with open("student.txt", "r") as file:
    print(file.readlines()) # here output will be in list format

# write() - Writes the specified string to the file

with open("student.txt", "w") as file:
    file.write("College: Cocsit\n")
    file.write("Laptop: Rog Asus Strix G16")

# writelines() - writes multiple strings

data = [
    "Arsalan\n",
    "Big Data\n"
    "Python\n"
]

with open("student.txt", "w") as file:
    file.writelines(data) # we can also write it as file.writelines(["Hello\n", "Python\n"])

# tell() - tells you the current position of the file courser.

with open("student.txt", "r") as file:
    print(file.tell())
    file.read(5)
    print(file.tell())

# seek()

with open("student.txt", "r") as file:
    print(file.read(5)) # Arsal
    file.seek(0) # cursor moves back
    print(file.read(5)) # prints Arsal

# redable() - it checks the weather the file is readable:

with open("student", "r") as file:
    print(file.readable()) # true

# writable() - checks whether the file is writable:

with open("student.txt", "w") as file:
    print(file.writable()) # true

# close()
# when using -
file = open("student.txt", "r")
# you should eventually :
file.close()
# But when you use:
with open("student.txt", "r") as file:
    print(file.read())

