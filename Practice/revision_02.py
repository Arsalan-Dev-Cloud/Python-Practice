# Write a program that asks the user for:
"""
Name
Age
"""

#Rules
"""input()
int()
variables
if
elif
else
comparison operators
and / or (if you need them)
f-string
"""

# And then apply the grades depending on marks
# And there is one condiiton that is Marks > 100  → Invalid Marks  &  Marks < 0    → Invalid Marks


# Output Should be like this 
"""
Enter Your Name: Arsalan
Enter Marks: 85

---------- Result ----------
Name                : Arsalan
Marks               : 85
Grade               : B
"""



# Program:-

name = input("Enter Your Name: ")
marks = int(input("Enter Marks: "))

print("------------Result-----------")
print(f"{'Name':<20}: {name}")
print(f"{'marks':<20}: {marks}")

if marks > 100 or marks < 0:
    print("Invalid Marks")
elif marks >= 90:
    print(f"{'Grade':<20}: A")
elif marks >= 80:
    print(f"{'Grade':<20}: B")
elif marks >= 70:
    print(f"{'Grade':<20}: C")
elif marks >= 60:
    print(f"{'Grade':<20}: D")
elif marks >= 50:
    print(f"{'Grade':<20}: E")
elif marks >= 40:
    print(f"{'Grade':<20}:F")
else:
    print("Failed")
