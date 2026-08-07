#---------multiple exceptions handling-----------------

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2
    print(result)

except ValueError:
    print("Invalid Number!")

except ZeroDivisionError:
    print("Cannot divide by Zero!")