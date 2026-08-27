"""
🎯 Task

Ask the user to enter 10 numbers and store them in a list.

Then your program should:

Display all numbers
Separate even and odd numbers
Separate positive and negative numbers
Find the total of even numbers
Find the total of odd numbers
Find the total of positive numbers
Find the total of negative numbers
Count how many even numbers
Count how many odd numbers
Find the highest number
Find the lowest number

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
Even_numbers = []
Odd_numbers = []
Positive_numbers = []
Negative_numbers = []
Even_count = 0
Odd_count = 0
for i in range(10):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

for number in numbers:
    if number % 2 == 0:
        Even_numbers.append(number)
        Even_count += 1
    else:
        Odd_numbers.append(number)
        Odd_count += 1

    if number > 0:
        Positive_numbers.append(number)
    else:
        Negative_numbers.append(number)

print("\n-------------------Report-------------------")
print(f"\n{'All Numbers':<20}: {numbers}")
print(f"\n{'Even Numbers':<20}: {Even_numbers}")
print(f"{'Odd Numbers':<20}: {Odd_numbers}")
print(f"\n{'Positive Numbers':<20}: {Positive_numbers}")
print(f"{'Negative Numbers':<20}: {Negative_numbers}")
print(f"\n{'Even Total':<20}: {sum(Even_numbers)}")
print(f"{'Odd Total':<20}: {sum(Odd_numbers)}")
print(f"\n{'Positive Total':<20}: {sum(Positive_numbers)}")
print(f"{'Negative Total':<20}: {sum(Negative_numbers)}")
print(f"\n{'Even Count':<20}: {Even_count}")
print(f"{'Odd Count':<20}: {Odd_count}")
print(f"\n{'Highest':<20}: {max(numbers)}")
print(f"{'Lowest':<20}: {min(numbers)}")

"""
Output:-

Output:- 
Enter number 1: 10
Enter number 2: -5
Enter number 3: 20
Enter number 4: 7
Enter number 5: -8
Enter number 6: 15
Enter number 7: 30
Enter number 8: -2
Enter number 9: 9
Enter number 10: 4

--------------- Result ---------------

All Numbers          : [10, -5, 20, 7, -8, 15, 30, -2, 9, 4]

Even Numbers         : [10, 20, -8, 30, -2, 4]
Odd Numbers          : [-5, 7, 15, 9]

Positive Numbers     : [10, 20, 7, 15, 30, 9, 4]
Negative Numbers     : [-5, -8, -2]

Even Total           : 54
Odd Total            : 26

Positive Total       : 95
Negative Total       : -15

Even Count           : 6
Odd Count            : 4

Highest              : 30
Lowest               : -8
"""