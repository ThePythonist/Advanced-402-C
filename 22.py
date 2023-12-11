import json

f = open("payments.json")
data = json.load(f)
for i in data["employees"]:
    print(i["name"],":",i["position"])
