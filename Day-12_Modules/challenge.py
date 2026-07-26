# ================================
# Day 12 Challenge
# Simple Calculator using Modules
# ================================

import calculator

print("===================================")
print("      SIMPLE CALCULATOR")
print("===================================")

num1 = float(input("Enter First Number  : "))
num2 = float(input("Enter Second Number : "))

print("\nChoose an Operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("\nEnter Your Choice (1-4): ")

if choice == "1":
    print(f"\nResult : {calculator.add(num1, num2)}")

elif choice == "2":
    print(f"\nResult : {calculator.subtract(num1, num2)}")

elif choice == "3":
    print(f"\nResult : {calculator.multiply(num1, num2)}")

elif choice == "4":
    if num2 == 0:
        print("\nError! Division by zero is not allowed.")
    else:
        print(f"\nResult : {calculator.divide(num1, num2)}")

else:
    print("\nInvalid Choice! Please select between 1 and 4.")