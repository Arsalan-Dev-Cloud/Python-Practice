#-------Program for *args---------

def add(*numbers):
    return sum(numbers)

print(add(10,20))
print(add(10,20,30))
print(add(50,30,20,40))
print(add(20,10,30,50,40,60,80,70,90))
print("\n")



#-------Loop through *args---------

def skills(*skills):
    for skill in skills:
        print(skill)

skills("Python", "SQL", "React", "FastAPI")
# Functions + Tuples + Loops.



# Output:- 
"""
30
60
140
450


Python
SQL
React
FastAPI
"""