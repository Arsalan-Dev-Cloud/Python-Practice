# This is a tuple in Python
# It is a symple program for tuple

fruits = ("apple", "banana", "cherry")
print(fruits) # ('apple', 'banana', 'cherry')

#--------------String tuple------------
Name = ("Arsalan", "Faizan", "Shoaib", "Noor")
print(Name) # ('Arsalan', 'Faizan', 'Shoaib', 'Noor')


#--------------Integer tuple-----------
Num = (10, 20, 30, 40, 50)
print(Num) # (10, 20, 30, 40, 50)

#--------------Mixed tuple-------------
student = ("Arsalan", 22, True, 85.5)
print(student) # ('Arsalan', 22, True, 85.5)


#------------Very Important------------
# Single-Element Tuple--
# Wrong:
number = (10) # Python treats it as an integer.

# Correct:
number = (10,) # The comma tells Python it's a tuple.
