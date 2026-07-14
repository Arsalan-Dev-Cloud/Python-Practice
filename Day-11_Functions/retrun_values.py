#-------------Function using return value---------------
def add(a, b):
    return a + b

result = add(10, 20)
print(result) # 30


# print() VS return
# Using print():-
def add(a, b):
    print(a + b)

result = add(10, 20)
print(result) # 30 
              # None


# Using return:-
def add(a, b):
    return a + b

result = add(10, 20)
print(result) # 30
