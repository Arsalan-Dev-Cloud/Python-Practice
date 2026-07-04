#using while loop 
secret_no = 4

while True:
    num = int(input("Guess the secret number between 1 and 10:"))

    if num == secret_no:
        print("Congratulations!")
        break
    else:
        print("Try again.")
    

#using for loop
secret_no = 4

for num in range(1, 11):
    num = int(input("Guess the secret number between 1 and 10:"))
    if num == secret_no:
        print("Congratulations!")
        break
    else:
        print("Try again.")
