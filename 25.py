import json

f1 = open("payments.json")
data = json.load(f1)


def solution1():
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

    sorted_salaries = dict(sorted(salaries.items(), key=lambda item: item[1]))
    f2 = open("sorted_salaries.json", "w")
    json.dump(sorted_salaries, f2, indent=2)


def solution2():
    sorted_payments = sorted(data["employees"], key=lambda item:sum(item['monthly_payment'].values()))
    f2 = open("sorted_payments.json", "w")
    json.dump(sorted_payments, f2, indent=4)


solution2()
