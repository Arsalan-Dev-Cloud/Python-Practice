#----------Vote access age check--------------
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
#-----------------------------------------------------
#---------Output 1---> Enter Your age: 25
#                      You are eligible to vote.
#-----------------------------------------------------
#---------Output 2---> Enter Your age: 15
#                      You are not eligible to vote.
#-----------------------------------------------------



#----------Check the number is odd or even------------
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
#---------------------------------------------------
#---------Output 1---> Enter a number: 20
#                      Even
#---------------------------------------------------
#---------Output 2---> Enter Your age: 15
#                      Odd
#---------------------------------------------------



#----------Check the grater number------------------
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("First number is larger.")
else:
    print("Second number is larger.")
#-----------------------------------------------------
#---------Output 1---> Enter first number: 20
#                      Enter second number: 30
#                      Second number is larger.
#------------------------------------------------------
#---------Output 2---> Enter first number: 100
#                      Enter second number: 50
#                      First number is larger.  
#------------------------------------------------------



#------------Check the Grades----------------
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 35:
    print("Grade D")
else:
    print("Fail")
#--------------------------------------------
#---------Output 1---> Enter marks: 95
#                      Grade A
#--------------------------------------------
#---------Output 1---> Enter marks: 65
#                      Grade C
#--------------------------------------------
#---------Output 2---> Enter marks: 25
#                      Fail
#--------------------------------------------
