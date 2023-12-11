import json

f = open("payments.json")
data = json.load(f)

count = 0

for i in data["employees"]:
    employee_salary = []
    for j in i["monthly_payment"].values():
        employee_salary.append(j)

    print(data["employees"][count]["name"], sum(employee_salary)/len(employee_salary))
    count += 1
