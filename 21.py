import json

f1 = open("states.json")
data = json.load(f1)
specials = []

for i in data["states"]:
    if i["name"] in ["Alaska","New York","Florida"] :
        specials.append(i)

f2 = open("special_states.json","w")
json.dump(specials,f2,indent=4)
