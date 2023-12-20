# import xmltodict
#
# xml_data = open("flights.xml").read()
#
# data_dict = xmltodict.parse(xml_data)
#
# flight_records = data_dict['flights']
# flights = flight_records['flight']
# toparis = {}
# id = 1
#
# for i in flights:
#     if i["destination"] == "Paris":
#         toparis.update({id: i})
#         id += 1
#
# for i, j in toparis.items():
#     print(i, ":", j)

# ---------------------------------------------------------------------------

import xmltodict
import dicttoxml

selected_flights = []
xml_data = open('flights.xml').read()
main_data = xmltodict.parse(xml_data)
for i in main_data['flights']['flight']:
    if i['destination'] == 'Paris':
        selected_flights.append(i)

selected_flights_xml = open('flightstoparis.xml', 'w')

selected_flights_to_xml = dicttoxml.dicttoxml(selected_flights)
print(type(selected_flights_to_xml))
selected_flights_xml.writelines(str(selected_flights_to_xml))
