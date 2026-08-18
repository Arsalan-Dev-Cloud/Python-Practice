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



# Output :-
"""
Enter number 1: 1 
Enter number 2: 2
Enter number 3: 3
Enter number 4: 4
Enter number 5: 5
Enter number 6: 6
Enter number 7: 7
Enter number 8: 8
Enter number 9: 9
Enter number 10: 10

---------------Result----------------
All Numbers         : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even Numbers        : [2, 4, 6, 8, 10]
Odd Numbers         : [1, 3, 5, 7, 9]
Even Total          : 30
Odd Total           : 25
Even Count          : 5
Odd Count           : 5
"""