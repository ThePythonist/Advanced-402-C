import xmltodict

xml_data = open("payments.xml").read()
xml_dict = xmltodict.parse(xml_data)

company = xml_dict["employees"]
employees = company["employee"]
pythons_salaries = []

for i in employees:
    if i["job_title"] == "Python Developer":
        for j in i["monthly_payment"].values():
            pythons_salaries.append(int(j))

avg = sum(pythons_salaries) / len(pythons_salaries)
print("Python Developer Average Salary :", avg)
