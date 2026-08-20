"""
Task

Ask the user to enter 10 numbers and store them in a list.

Then display:

All numbers
Positive numbers
Negative numbers
Even numbers
Odd numbers
Total of all numbers
Highest number
Lowest number
"""
"""
Rules:-
input()
int()
variables
list
append()
for loop
if / else
sum()
max()
min()
f-string
"""

# Program :-

numbers = []
positive_numbers = []
negative_numbers = []
even_numbers = []
odd_numbers = []

for i in range(10):
    number = int(input(f"Enter Number {i + 1}: "))
    numbers.append(number)

for number in numbers:
    if number > 0:
        positive_numbers.append(number)
    else:
        negative_numbers.append(number)

    if number % 2 == 0:
            even_numbers.append(number)
    else:
            odd_numbers.append(number)

print("\n---------------------Report---------------------")
print(f"\n{'All Numbers':<20}: {numbers}")
print(f"\n{'Positive numbers':<20}: {positive_numbers}")
print(f"\n{'Negative Numbers':<20}: {negative_numbers}")
print(f"\n{'Even Numbers':<20}: {even_numbers}")
print(f"\n{'Odd Numbers':<20}: {odd_numbers}")
print(f"\n{'Total':<20}: {sum(numbers)}")
print(f"\n{'Highest':<20}: {max(numbers)}")
print(f"\n{'Lowest':<20}: {min(numbers)}")


# Output :-
"""
Enter Number 1: 2
Enter Number 2: 3
Enter Number 3: -4
Enter Number 4: -6
Enter Number 5: -6
Enter Number 6: -7
Enter Number 7: 3
Enter Number 8: 5
Enter Number 9: -4
Enter Number 10: -9

---------------------Report---------------------

All Numbers         : [2, 3, -4, -6, -6, -7, 3, 5, -4, -9]

Positive numbers    : [2, 3, 3, 5]

Negative Numbers    : [-4, -6, -6, -7, -4, -9]

Even Numbers        : [2, -4, -6, -6, -4]

Odd Numbers         : [3, -7, 3, 5, -9]

Total               : -23

Highest             : 5

Lowest              : -9
"""