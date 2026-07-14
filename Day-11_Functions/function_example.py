#----------Real World Example-----------

# Find Odd and Even:-
def check_num(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
number = int(input("Enter the number:"))
print("The Entered Number is",check_num(number))

# Output:-
        # out 1-
            # Enter the number:10
            # The Entered Number is Even

        # out 2-
            #Enter the number:33
            #The Entered Number is Odd


# Grade Calculator:-

def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    return "F"

print(grade(87)) # B


# Area of Rectangle:-
def area(length, width):
    return length * width

print(area(10, 5)) # 50
