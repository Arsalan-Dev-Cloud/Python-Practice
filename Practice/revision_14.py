"""
Task

Ask the user to enter 10 numbers and store them in a list.

Then your program should find how many times each number appears.

Display:

All numbers
Each different number
Its occurrence
Its positions/indexes
The highest-occurring number
How many times it occurred

Rules:-

input()
int()
variables
lists
append()
for
nested for
if / elif / else
len()
f-string
"""

numbers = []
unique_numbers = []
highest_occur = 0
frequent = []
for i in range(10):
    number = int(input(f"Enter Number {i + 1}: "))
    numbers.append(number)

# Find different numbers
for i in range(len(numbers)):
    if numbers[i] not in unique_numbers:
        unique_numbers.append(numbers[i])

print("\n------------------------------------Report-------------------------------------")
print(f"\n{'All Numbers':<20}: {numbers}")

# Find occurrence and positions
for j in range(len(unique_numbers)):
    position = []
    for i in range(len(numbers)):
        if unique_numbers[j] == numbers[i]:
            position.append(i)
    occurrence = len(position)

    # Find highest occurrence
    if occurrence > highest_occur:
        highest_occur = occurrence
    print(f"\n{unique_numbers[j]} → Occurrence : {occurrence}")
    print(f"{unique_numbers[j]} → Positions  : {position}")

# Find all most frequent numbers
for j in range(len(unique_numbers)):
    position = []
    for i in range(len(numbers)):
        if unique_numbers[j] == numbers[i]:
            position.append(i)
    occurrence = len(position)
    if occurrence == highest_occur:
        frequent.append(unique_numbers[j])
print(f"\n{'Highest Occurrence':<20}: {highest_occur}")
print(f"{'Most Frequent':<20}: {frequent}")

# Output:-

"""
Enter Number 1: 10
Enter Number 2: 20
Enter Number 3: 30
Enter Number 4: 10
Enter Number 5: 20
Enter Number 6: 10
Enter Number 7: 20
Enter Number 8: 40
Enter Number 9: 50
Enter Number 10: 60

------------------------------------Report-------------------------------------

All Numbers         : [10, 20, 30, 10, 20, 10, 20, 40, 50, 60]

10 → Occurrence : 3
10 → Positions  : [0, 3, 5]

20 → Occurrence : 3
20 → Positions  : [1, 4, 6]

30 → Occurrence : 1
30 → Positions  : [2]

40 → Occurrence : 1
40 → Positions  : [7]

50 → Occurrence : 1
50 → Positions  : [8]

60 → Occurrence : 1
60 → Positions  : [9]

Highest Occurrence  : 3
Most Frequent       : [10, 20]
"""