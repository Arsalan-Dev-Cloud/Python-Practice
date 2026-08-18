"""
Task

Ask the user to enter 10 numbers and store them in a list.

Then ask the user to enter one more number to search for.

Your program must display:

All numbers
Whether the searched number exists or not
How many times it appears
The positions/indexes where it appears
"""

# Program:-

numbers = []
position = []
count = 0

for i in range(10):
    number = int(input(f"Enter Number {i + 1}: "))
    numbers.append(number)

search_no = int(input("\nEnter the number to search: "))

for i in range(len(numbers)):
    if search_no == numbers[i]:
        count =+ 1
        position.append(i)

# ----------------OR we can USE------------------           - - so here either you can use upper for loop or lower for loop

"""for number in numbers:

    if search_no == number:       
        count += 1 """


if count > 0:
    y_n = "Yes"
else:
    y_n = "No"
        

print("\n--------------Result--------------")
print(f"{'Numbers':<20}: {numbers}")
print(f"{'Number Found':<20}: {y_n}")
print(f"{'Occurrence':<20}: {count}")
print(f"{'Position':<20}: {position}")