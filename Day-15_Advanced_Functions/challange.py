#---------------CHALLANGE-----------------

employees = [
    {"name": "Arsalan", "salary": 60000},
    {"name": "Ali", "salary": 45000},
    {"name": "Shoaib", "salary": 75000},
    {"name": "Ahmed", "salary": 35000}
]


print(employees)

condition_salary = list(
    filter(lambda employee: employee["salary"] >= 50000, employees)
)
print(condition_salary)

salary_increase = list(
    map(lambda employee: employee["salary"] + (employee["salary"] * 10 / 100), employees)
)
print(salary_increase)

salaries = []

for employee in employees:
    salaries.append(employee["salary"])

print(salaries)

def tot_mult_salary(*salaries):
    total_salary = sum(salaries)
    return total_salary

print("Total Salary:", tot_mult_salary(*salaries))


def display_employee(**details):
    for key, value in details.items():
        print(f"{key:<10}: {value}")


for employee in employees:
    display_employee(**employee)
    print()


# Output:-

"""
[{'name': 'Arsalan', 'salary': 60000}, {'name': 'Ali', 'salary': 45000}, {'name': 'Shoaib', 'salary': 75000}, {'name': 'Ahmed', 'salary': 35000}]
[{'name': 'Arsalan', 'salary': 60000}, {'name': 'Shoaib', 'salary': 75000}]
[66000.0, 49500.0, 82500.0, 38500.0]
[60000, 45000, 75000, 35000]
Total Salary: 215000
name      : Arsalan
salary    : 60000

name      : Ali
salary    : 45000

name      : Shoaib
salary    : 75000

name      : Ahmed
salary    : 35000
"""