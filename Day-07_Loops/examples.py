# print numbers from 1 to 10 using for loop
for i in range(1, 11):
    print(i)


# sum of numbers 
total = 0
for i in range(1, 6):
    total += i

print("Sum of numbers from 1 to 5 is:", total)


# Multiplication table 
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


# coundown Timer
count = 10
while count > 0:
    print(count)
    count -= 1 # count = count -1

print("lift off!")
