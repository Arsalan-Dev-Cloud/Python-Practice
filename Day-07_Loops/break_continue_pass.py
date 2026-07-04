# use of break Statement
# it is used to stop the loop immediately when the condition is met
for i in range(10):
    if i == 5:
        break
    print(i)

# use of continue Statement
# it is used to skip the current iteration of the loop and continue with the next iteration
for i in range(6):
    if i == 3:
        continue
    print(i)

# use of pass Statement
# it is used as a placeholder for future code. When the pass statement is executed, nothing
for i in range(5):
    if i == 2:
        pass
    print(i)
