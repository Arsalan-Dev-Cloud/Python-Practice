# Ask the user to Enter 5 numbers and store it in a list and then find the hightest, lowest, total and average.
values = []
for i in range(5):
    value = int(input((f"Enter Number {i + 1} : ")))
    values.append(value)

total = sum(values)
average = total / len(values)
highest = max(values)
lowest = min(values)

print("\n-------------Result-------------")

print(f"{'Number':<20}: {values}")
print(f"{'Total':<20}: {total}")
print(f"{'Average':<20}: {average:.2f}")
print(f"{'Highest':<20}: {highest}")
print(f"{'Lowest':<20}: {lowest}")

# Output:-
"""
Enter Number 1 : 10
Enter Number 2 : 20
Enter Number 3 : 30
Enter Number 4 : 40
Enter Number 5 : 50

-------------Result-------------
Number              : [10, 20, 30, 40, 50]
Total               : 150
Average             : 30.00
Highest             : 50
Lowest              : 10
"""