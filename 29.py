import xmltodict
import dicttoxml
xml_data = open("flights.xml").read()

data_dict = xmltodict.parse(xml_data)

flight_records = data_dict['flights']
flights = flight_records['flight']

william_thompson_flights = []

for i in flights:
    for j in i["passengers"]["passenger"]:
        if j["name"] == "William Thompson":
            william_thompson_flights.append(i)

for i in william_thompson_flights:
    print(i)

selected_flights_xml = open('williamflights.xml', 'w')

selected_flights_to_xml = dicttoxml.dicttoxml(william_thompson_flights)
print(type(selected_flights_to_xml))
selected_flights_xml.writelines(str(selected_flights_to_xml))
