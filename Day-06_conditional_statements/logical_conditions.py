# There are basically three types of locial codnitions which are - and , or, not.
#---------------Program for 'and' logical condition------------------
age = 25
salary = 30000

if age >= 21 and salary >= 25000:
    print("Loan Approved")
#----------output--> Loan Approved


#---------------Program for 'or' logical condition-------------------
attendance = 80
medical_certificate = False

if attendance >= 75 or medical_certificate:
    print("Allowed to take exam")
#---------output--> Allowed to take exam


#--------------Program for 'not' logial condition--------------------
is_logged_in = False

if not is_logged_in:
    print("Please log in")
#---------output--> Please Log in
