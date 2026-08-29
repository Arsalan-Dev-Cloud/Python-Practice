"""
🎯 Task

Ask the user to enter 10 numbers and store them in a list.

Your program should display:

All numbers
Highest number
Second highest number
Lowest number
Second lowest number
Position/index of the highest number
Position/index of the lowest number

Rules:-

input()
int()
variables
list
append()
for loop
if / elif / else
max()
min()
len()
f-string
"""

numbers = []
highest = 0
second_highest = 0
lowest = 0
second_lowest = 0
highest_position = 0
lowest_position = 0


# Take 10 numbers
for i in range(10):
    number = int(input(f"Enter Number {i + 1}: "))
    numbers.append(number)

# Find Highest and Second Highest
for i in range(len(numbers)):
    count = 0
    for j in range(len(numbers)):
        if numbers[i] >= numbers[j] and i != j:
            count += 1
    if count == 9:
        highest = numbers[i]
        highest_position = i
    elif count == 8:
        second_highest = numbers[i]

# Find Lowest and Second Lowest
for i in range(len(numbers)):
    count = 0
    for j in range(len(numbers)):
        if numbers[i] <= numbers[j] and i != j:
            count += 1
    if count == 9:
        lowest = numbers[i]
        lowest_position = i
    elif count == 8:
        second_lowest = numbers[i]

print("\n--------------- Result ---------------")
print(f"{'All Numbers':<20}: {numbers}")
print(f"{'Highest':<20}: {highest}")
print(f"{'Second Highest':<20}: {second_highest}")
print(f"{'Lowest':<20}: {lowest}")
print(f"{'Second Lowest':<20}: {second_lowest}")
print(f"{'Highest Position':<20}: {highest_position}")
print(f"{'Lowest Position':<20}: {lowest_position}")

# Output:-

"""
Enter Number 1: 40
Enter Number 2: 5
Enter Number 3: 6
Enter Number 4: 70
Enter Number 5: 40
Enter Number 6: 50
Enter Number 7: 20
Enter Number 8: 30
Enter Number 9: 80
Enter Number 10: 90

--------------- Result ---------------
All Numbers         : [40, 5, 6, 70, 40, 50, 20, 30, 80, 90]
Highest             : 90
Second Highest      : 80
Lowest              : 5
Second Lowest       : 6
Highest Position    : 9
Lowest Position     : 1
"""