"""try:
    # risky code

except:
    # run if something goes wrong"""

#--------------Program for expction handling-------------------

try:
    num= int(input("Enter number: "))
    print(100 / num)

except :
    print("Something went wrong")

#---------------------------------------------------------------

try:
    num =int(input("Enter number: "))
    print(100 / num)

except ValueError:
    print("please enter number only")

except ZeroDivisionError:
    print("You cannot divide by zero.")