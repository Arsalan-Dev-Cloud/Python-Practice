"""
Ask the user to enter 10 numbers and store them in a list.

Then find and display:

All numbers
Even numbers
Odd numbers
Total of even numbers
Total of odd numbers
Count of even numbers
Count of odd numbers
"""

numbers = []
even_numbers = []
odd_numbers = []

for i in range(10):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

"""for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even_numbers.append(numbers[i])              
    else:
        odd_numbers.append(numbers[i])"""

#----------------OR we can USE--------------------   - so here either you can use upper for loop or lower for loop

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)


even_total = sum(even_numbers)
odd_total = sum(odd_numbers)

even_count = len(even_numbers)
odd_count = len(odd_numbers)

print("\n---------------Result----------------")
print(f"{'All Numbers':<20}: {numbers}")
print(f"{'Even Numbers':<20}: {even_numbers}")
print(f"{'Odd Numbers':<20}: {odd_numbers}")
print(f"{'Even Total':<20}: {even_total}")
print(f"{'Odd Total':<20}: {odd_total}")
print(f"{'Even Count':<20}: {even_count}")
print(f"{'Odd Count':<20}: {odd_count}")
