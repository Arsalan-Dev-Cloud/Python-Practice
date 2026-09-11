"""
Task

Ask the user to enter 10 numbers and store them in a list.

Then separate the numbers based on their index position:

Numbers at even indexes → even_position
Numbers at odd indexes → odd_position

Also calculate:

Total of even-position numbers
Total of odd-position numbers
Highest number from even positions
Highest number from odd positions
Lowest number from even positions
Lowest number from odd positions

Rules:-
input()
int()
list
append()
for
if / else
len()
%
sum()
max()
min()
f-string
"""

# Program:-

numbers = []
even_position = []
odd_position = []

for i in range(10):
    number = int(input(f"Enter Number {i + 1}: "))
    numbers.append(number)

for i in range(len(numbers)):
    if i % 2 == 0:
        even_position.append(numbers[i])
    else:
        odd_position.append(numbers[i])

for i in range(len(even_position)):
    highest_count = 0
    lowest_count = 0
    for j in range(len(even_position)):
        if even_position[i] >= even_position[j] and  i != j:
            highest_count += 1
        if even_position[i] <= even_position[j] and i != j:
            lowest_count += 1

    if highest_count == len(even_position) - 1:
        even_highest = even_position[i]
    if lowest_count == len(even_position) - 1:
        even_lowest = even_position[i]
    

for i in range(len(odd_position)):
    highest_count = 0
    lowest_count = 0
    for j in range(len(odd_position)):
        if odd_position[i] >= odd_position[j] and i != j:
            highest_count += 1    
        if odd_position[i] <= odd_position[j] and i != j:
            lowest_count += 1    

    if highest_count == len(odd_position) -1:
        odd_highest = odd_position[i]
    if lowest_count == len(odd_position) - 1:
            odd_lowest = odd_position[i]

print("\n------------------------------- Result -------------------------------")
print(f"\n{'All Numbers':<20}: {numbers}")
print(f"\n{'Even Position':<20}: {even_position}")
print(f"{'Odd Position':<20}: {odd_position}")
print(f"\n{'Even Position Total':<20}: {sum(even_position)}")
print(f"{'Odd Position Total':<20}: {sum(odd_position)}")
print(f"\n{'Even Position Highest':<20}: {even_highest}")
print(f"{'Odd Position Highest':<20}: {odd_highest}")
print(f"\n{'Even Position Lowest':<20}: {even_lowest}")
print(f"{'Odd Position Lowest':<20}: {odd_lowest}")

# Output:-
"""
Enter Number 1: 10
Enter Number 2: 30
Enter Number 3: 35
Enter Number 4: 25
Enter Number 5: 77
Enter Number 6: 68
Enter Number 7: 37
Enter Number 8: 20
Enter Number 9: 90
Enter Number 10: 67

------------------------------- Result -------------------------------

All Numbers         : [10, 30, 35, 25, 77, 68, 37, 20, 90, 67]

Even Position       : [10, 35, 77, 37, 90]
Odd Position        : [30, 25, 68, 20, 67]

Even Position Total : 249
Odd Position Total  : 210

Even Position Highest: 90
Odd Position Highest: 68

Even Position Lowest: 10
Odd Position Lowest : 20
"""