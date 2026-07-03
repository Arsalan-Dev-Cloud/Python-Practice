# An if statement inside another if statement
#------------------Program for Nested if----------------------
age = 25
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to vote")
    else:
        print("Not a Citizen")
else:
    print("Underage")


#--------------Output--------------
Elibile to vote
