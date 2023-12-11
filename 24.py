import json

f = open("payments.json")
data = json.load(f)
salaries = {}
count = 0

for i in data["employees"]:
    employee_salary = []
    for j in i["monthly_payment"].values():
        employee_salary.append(j)

    avg = sum(employee_salary) / len(employee_salary)
    name = data["employees"][count]["name"]
    salaries.setdefault(name, avg)
    count += 1

print(salaries)
most_payed = max(salaries.values())
for i in salaries:
    if salaries[i] == most_payed:
        print("Most Payed Employee :", i, most_payed)
