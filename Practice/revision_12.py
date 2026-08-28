"""
🎯 Task

Ask the user to enter 10 numbers and store them in a list.

Then your program should find:

All numbers entered
Numbers that appear more than once
How many times each repeated number appears
The positions/indexes of each repeated number
Numbers that appear only once

Rules:-
input()
int()
list
append()
for
if / elif / else
len()
"""

# Program:-

numbers = []
duplicate_numbers = []
once_numbers = []

for i in range(10):
    number = int(input(f"Enter Number {i + 1}: "))
    numbers.append(number)

for i in range(len(numbers)):
    for j in range(len(numbers)):
        if numbers[i] == numbers[j] and i != j:
            if numbers[i] not in duplicate_numbers:
                duplicate_numbers.append(numbers[i])

for number in numbers:
    if number not in duplicate_numbers:
        once_numbers.append(number)


print("\n-----------------Report------------------")
print(f"{'All Numbers':<20}: {numbers}")
print(f"\n{'Duplicate Numbers':<20}: {duplicate_numbers}")
for j in range(len(duplicate_numbers)):
    position = []
    for i in range(len(numbers)):
        if duplicate_numbers[j] == numbers[i]:
            position.append(i)
    print(f"\n{duplicate_numbers[j]} → Occurrence : {len(position)}")
    print(f"{duplicate_numbers[j]} → Positions  : {position}")
print(f"\n{'Unique Numbers':<20}: {once_numbers}")

#-------------------------------------------------------------------------------OR----------------------------------------------------------------------------

numbers = []
duplicate_numbers = []
once_numbers = []

# Take 10 numbers
for i in range(10):
    number = int(input(f"Enter Number {i + 1}: "))
    numbers.append(number)

# Find duplicate numbers and unique numbers
for i in range(len(numbers)):
    count = 0
    for j in range(len(numbers)):
        if numbers[i] == numbers[j]:
            count += 1
    if count > 1:
        if numbers[i] not in duplicate_numbers:
            duplicate_numbers.append(numbers[i])
    else:
        once_numbers.append(numbers[i])

# Display result
print("\n-----------------Report------------------")
print(f"{'All Numbers':<20}: {numbers}")
print(f"\n{'Duplicate Numbers':<20}: {duplicate_numbers}")

# Find positions and occurrence of duplicate numbers
for j in range(len(duplicate_numbers)):
    position = []
    for i in range(len(numbers)):
        if duplicate_numbers[j] == numbers[i]:
            position.append(i)
    print(f"\n{duplicate_numbers[j]} → Occurrence : {len(position)}")
    print(f"{duplicate_numbers[j]} → Positions  : {position}")
print(f"\n{'Unique Numbers':<20}: {once_numbers}")


#--------------------------------------------------------------------------------------OUTPUT---------------------------------------------------------------------------------


"""
Output:-

Enter Number 1: 10
Enter Number 2: 20
Enter Number 3: 30
Enter Number 4: 10
Enter Number 5: 10
Enter Number 6: 20
Enter Number 7: 60  
Enter Number 8: 70
Enter Number 9: 80
Enter Number 10: 10

-----------------Report------------------
All Numbers         : [10, 20, 30, 10, 10, 20, 60, 70, 80, 10]

Duplicate Numbers   : [10, 20]

10 → Occurrence : 4
10 → Positions  : [0, 3, 4, 9]

20 → Occurrence : 2
20 → Positions  : [1, 5]

Unique Numbers      : [30, 60, 70, 80]
"""