#-------------else and finally in try except block-----------------

# Else:-
try:
    num = int(input("Enter number: "))

except ValueError:
    print("Invalid input!")

else:
    print("You entered:", num)

#---------------------------------------------------------------

# Finally:-
try:
    num = int(input("Enter number: "))
    print(num)

except ValueError:
    print("Invalid input!")

finally:
    print("Program Finished.")

#---------------------------------------------------------------

# Using else and finally together:-
try:
    num = int(input("Enter number: ")) 
    print(num)
except ValueError:
    print("Invalid input!")
else:
    print("You entered:", num)
finally:
    print("Program Finished.")