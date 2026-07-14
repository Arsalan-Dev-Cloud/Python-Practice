#---------Default Argurments-------------

def greet(name="Guest"):
    print(f"Hello, {name}")

greet()
greet("Arsalan")

# Output:- 
# Hello, Guest
# Hello, Arsalan


#----------Keyword Arguments------------

def student(name, age):
    print(name)
    print(age)

student(age=22, name="Arsalan")

# Output:-
# Arsalan
# 22


#------------Variable length Argument-------------
 
def add(*numbers):
    print(numbers)

add(10, 20, 30, 40) # (10, 20, 30, 40)

def add(*numbers):
    total = sum(numbers)
    return total

print(add(10, 20, 30))  # 60


