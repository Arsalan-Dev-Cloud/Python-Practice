#Create an ATM Login System.

account_pin = 999
pin = int(input("Enter the Pin:"))

if pin == account_pin:
    print("Welcome to Your account.")
else:
    print("Invalid PIN.")
#---------------------------------------------------
#---------output 1---> Enter the Pin: 578
#                      Invalid PIN.
#---------------------------------------------------
#---------output 2---> Enter the Pin: 999
#                      Welcome to Your account.
#---------------------------------------------------
