"""
🎯 Task

Ask the user to enter 10 numbers and store them in a list.

Then ask the user to enter one number to remove.

Your program should:

Display all original numbers.
Check whether the number exists.
Count how many times it appears.
Display all indexes where it appears.
Create a new list containing all numbers except the searched number.
Display the new list.
Display:
Total of original numbers
Total of new numbers
Highest number in new list
Lowest number in new list

Rules:-

input()
int()
variables
list
append()
for loop
if / elif / else
sum()
max()
min()
len()
f-string
"""

numbers = []
position = []
count = 0
New_numbers = []
for i in range(10):
    number = int(input(f"Enter Number {i + 1}: "))
    numbers.append(number)

Remove_number = int(input("\nEnter Number To Remove: "))

for i in range(len(numbers)):
    if numbers[i] == Remove_number:
        count += 1
        position.append(i)

    if numbers[i] != Remove_number:
        New_numbers.append(numbers[i])

if count > 0:
    y_n = "Yes"
else:
    y_n = "No"


print("\n-----------------Report---------------")
print(f"\n{'Original Numbers':<20}: {numbers}")
print(f"\n{'Number To Remove':<20}: {Remove_number}")
print(f"{'Number Found':<20}: {y_n}")
print(f"{'Occurrence':<20}: {count}")
print(f"{'Positions':<20}: {position}")
print(f"\n{'New Numbers':<20}: {New_numbers}")
print(f"\n{'Original Total':<20}: {sum(numbers)}")
print(f"{'New Total':<20}: {sum(New_numbers)}")
print(f"\n{'New Highest':<20}: {max(New_numbers)}")
print(f"{'New Lowest':<20}: {min(New_numbers)}")

"""
Output:-

Enter Number 1: 10
Enter Number 2: 20
Enter Number 3: 30
Enter Number 4: 40
Enter Number 5: 10
Enter Number 6: 20
Enter Number 7: 50
Enter Number 8: 60
Enter Number 9: 40
Enter Number 10: 10

Enter Number To Remove: 10

-----------------Report---------------

Original Numbers    : [10, 20, 30, 40, 10, 20, 50, 60, 40, 10]

Number To Remove    : 10
Number Found        : Yes
Occurrence          : 3
Positions           : [0, 4, 9]

New Numbers         : [20, 30, 40, 20, 50, 60, 40]

Original Total      : 290
New Total           : 260

New Highest         : 60
New Lowest          : 20

"""