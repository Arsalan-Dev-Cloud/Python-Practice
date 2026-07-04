# A for loop is used when you know how many times you want to repeat somthing.
# Syntax - for variable in sequence:
#               #code

# to print the numbers from 0 to 4
for i in range(5):
    print(i)

# use of range(stop) function 
for i in range(5):
    print(i)

# use of range(start, stop) function
for i in range(1,6):
    print(i)

# use of range(start, stop, step) function
for i in range(2, 11, 2):
    print(i)

# use of range() function with negative step
for i in range(10, 0, -1):
    print(i)

#Loop through a string
name = "Arsalan"

for letter in name:
    print(letter)

#Loop through a list
fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits:
    print(fruit)
