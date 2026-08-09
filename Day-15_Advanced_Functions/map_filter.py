#-----------Program for python using map()------------

numbers = [1,2,3,4,5]

square = list(
    map(lambda x: x * x, numbers)    
)

print(square)  # [1, 4, 9, 16, 25]


#---------------------------------------------------
marks = [45, 92, 78, 33, 85, 25]

passed = list(
    filter(lambda mark: mark >= 35, marks)
)
print(passed)  # [45, 92, 78, 85]



#----------Program for python using filter()-----------

numbers = [1,2,3,4,5,6]

even_number = list(
    filter(lambda x: x % 2 == 0, numbers)
)

print(even_number)  # [2, 4, 6]

#-------------------------------------------------------

update = list(
    map(lambda mark: mark + 5, marks)
)
print(update)  # [50, 97, 83, 38, 90, 30]