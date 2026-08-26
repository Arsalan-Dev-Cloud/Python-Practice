"""
Task

Ask the user to enter 10 numbers and store them in a list.

Then ask the user to enter one number to search for.

Your program should display:

All numbers
Whether the number was found
How many times it appears
All indexes where it appears
Sum of all occurrences
Highest occurrence value
Lowest occurrence value

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
count = 0
position = []
occurrence_numbers = []
for i in range(10):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

search_num = int(input("Enter the number for Search: "))

for i in range(len(numbers)):
    if search_num == numbers[i]:
        count += 1
        position.append(i)
        occurrence_numbers.append(numbers[i])

if count > 0:
    y_n = "Yes"
else:
    y_n = "No"

print("\n---------------Report----------------")
print(f"{'All Numbers':<20}: {numbers}")
print(f"{'Search Number':<20}: {search_num}")
print(f"{'Number Found':<20}: {y_n}")
print(f"{'Occurrence':<20}: {count}")
print(f"{'Position':<20}: {position}")
print(f"{'Occurance Total':<20}: {sum(occurrence_numbers)}")
print(f"{'Heighest':<20}: {max(occurrence_numbers)}")
print(f"{'Lowest':<20}: {min(occurrence_numbers)}")


"""
Enter number 1: 10
Enter number 2: 20
Enter number 3: 30
Enter number 4: 30
Enter number 5: 40
Enter number 6: 50
Enter number 7: 40
Enter number 8: 40
Enter number 9: 30
Enter number 10: 10
Enter the number for Search: 40

---------------Report----------------
All Numbers         : [10, 20, 30, 30, 40, 50, 40, 40, 30, 10]
Search Number       : 40
Number Found        : Yes
Occurrence          : 3
Position            : [4, 6, 7]
Occurance Total     : 120
Heighest            : 40
Lowest              : 40
"""