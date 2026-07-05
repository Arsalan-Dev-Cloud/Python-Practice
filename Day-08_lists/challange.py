#-------ask a user to enter marks for 5 subjects and store it in a list and then find the highest marks, lowest marks, total marks and average marks.
subjects = ["Math", "Science", "English", "History", "Geography"]
marks = []
for i in range(5):
    mark = int(input(f"Enter marks for {subjects[i]}: "))
    marks.append(mark)

highest = max(marks)
lowest = min(marks)
total = sum(marks)
average = total / len(marks)

print("\n----- Student Marks Report -----")
for i in range(len(subjects)):
    print(f"{subjects[i]:<10}: {marks[i]}")


print("-"*30)
print(f"Highest Marks: {highest}")
print(f"Lowest Marks: {lowest}")
print(f"Total Marks: {total}")
print(f"Average Marks: {average:.2f}")

if average >= 90:
    print("Grade: A")
elif average >= 80:
    print("Grade: B")
elif average >= 70:
    print("Grade: C")
elif average >= 60:
    print("Grade: D")
else:
    print("Grade: F")
