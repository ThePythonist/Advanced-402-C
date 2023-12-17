import xmltodict

# XML data to be parsed
xml_data = open("flights.xml").read()

# Parse XML data into a dictionary
data_dict = xmltodict.parse(xml_data)

# Access the parsed data
flight_records = data_dict['flights']
flights = flight_records['flight']

for i in flights:
    print(i)
