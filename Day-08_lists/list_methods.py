#----------list methods-----------
fruits = ["Apple","Banana","Mango"]
fruits[1] = "Orange"
print(fruits) # ["Apple", "Orange", "Mango"]
#------------------------------------------------

# Append method
fruits = ["Apple","Banana"]
fruits.append("Mango")
print(fruits) # ["Apple", "Banana", "Mango"]
#------------------------------------------------

# Insert method
fruits.insert(1,"Orange")
print(fruits) # ["Apple", "Orange", "Banana", "Mango"]
#------------------------------------------------

# exted method
list1 = [1,2,3]
list2 = [4,5,6]
list1.extend(list2)
print(list1) # [1,2,3,4,5,6]
#------------------------------------------------

# Remove method
fruits.remove("Banana")
print(fruits) # ["Apple", "Orange", "Mango"]
#------------------------------------------------

# Pop method
fruits.pop(1)
print(fruits) # ["Apple", "Mango"]
#------------------------------------------------

# del method
del fruits[0]
print(fruits) # ["Mango"]
#------------------------------------------------

# Clear method
fruits.clear()
print(fruits) # [] -- all elements are removed
#------------------------------------------------

# List length
numbers = [10,20,30,40,50]
print(len(numbers)) # 5
#------------------------------------------------

# use for loop to iterate through a list
fruits = ["Apple","Banana","Mango"]
for fruit in fruits:
    print(fruit)   # Apple
                   # Banana
                   # Mango
#------------------------------------------------

# Membership operator
fruits = ["Apple","Banana","Mango"]
print("Apple" in fruits) # True
print("Orange" in fruits) # False
#------------------------------------------------

# Sorting a list
numbers = [50,20,10,40,30]
numbers.sort()
print(numbers) # [10,20,30,40,50]
#------------------------------------------------

# reversing a list
numbers = [50,20,10,40,30]
numbers.reverse()  
print(numbers) # [30,40,10,20,50]
#------------------------------------------------

# copying a list
numbers = [10,20,30,40,50]
numbers_copy = numbers.copy()
print(numbers_copy) # [10,20,30,40,50]
#------------------------------------------------

# counting the number of occurrences of an element in a list
numbers = [10,20,30,10,40,50,10]
print(numbers.count(10)) # 3
#------------------------------------------------

# finding the index of an element in a list
numbers = [10,20,30,40,50]
print(numbers.index(30)) # 2
#------------------------------------------------
