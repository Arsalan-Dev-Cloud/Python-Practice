"""
Task

Ask the user to enter 10 numbers and store them in a list.

Then calculate and display:

All numbers
Total
Average
Highest number
Lowest number
How many numbers are greater than the average
How many numbers are less than the average
How many numbers are equal to the average

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
f-string
"""

# Program:-

numbers = []
gre_avg_count = 0
les_avg_count = 0
equ_avg_count = 0

for i in range(10):
    number = int(input(f"Enter Number {i + 1}: "))
    numbers.append(number)

total = sum(numbers)
average = total / len(numbers)
highest = max(numbers)
lowest = min(numbers)

for i in range(len(numbers)):
    if numbers[i] > average:
        gre_avg_count += 1

    if numbers[i] < average:
        les_avg_count += 1

    if numbers[i] == average:
        equ_avg_count += 1

print("\n--------------Report--------------")
print(f"{'All Numbers':<20}: {numbers}")
print(f"{'Total':<20}: {total}")
print(f"{'Average':<20}: {average}")
print(f"{'Highest':<20}: {highest}")
print(f"{'Lowest':<20}: {lowest}")
print(f"{'Greater than Average':<20}: {gre_avg_count}")
print(f"{'Less than Average':<20}: {les_avg_count}")
print(f"{'Equal to Average':<20}: {equ_avg_count}")


# Output:-
"""
Enter Number 1: 10
Enter Number 2: 20
Enter Number 3: 30
Enter Number 4: 40
Enter Number 5: 50
Enter Number 6: 60
Enter Number 7: 70
Enter Number 8: 80
Enter Number 9: 90
Enter Number 10: 100

--------------Report--------------
All Numbers         : [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Total               : 550
Average             : 55.0
Highest             : 100
Lowest              : 10
Greater than Average: 5
Less than Average   : 5
Equal to Average    : 0
"""
