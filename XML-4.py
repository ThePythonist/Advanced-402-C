import xml.etree.ElementTree as ET

# XML data
xml_data = '''
<airline>
  <flight>
    <flight_number>FL001</flight_number>
    <origin>New York</origin>
    <destination>London</destination>
    <departure_date>2023-12-01</departure_date>
    <departure_time>10:00</departure_time>
    <arrival_date>2023-12-01</arrival_date>
    <arrival_time>17:30</arrival_time>
    <duration>7 hours 30 minutes</duration>
    <aircraft_type>Boeing 747</aircraft_type>
    <passengers>
      <passenger>
        <name>John Smith</name>
        <age>35</age>
      </passenger>
      <passenger>
        <name>Jane Doe</name>
        <age>28</age>
      </passenger>
    </passengers>
  </flight>
  <flight>
    <flight_number>FL002</flight_number>
    <origin>London</origin>
    <destination>Paris</destination>
    <departure_date>2023-12-02</departure_date>
    <departure_time>09:30</departure_time>
    <arrival_date>2023-12-02</arrival_date>
    <arrival_time>15:45</arrival_time>
    <duration>6 hours 15 minutes</duration>
    <aircraft_type>Airbus A380</aircraft_type>
    <passengers>
      <passenger>
        <name>Michael Johnson</name>
        <age>42</age>
      </passenger>
      <passenger>
        <name>Sarah Williams</name>
        <age>30</age>
      </passenger>
    </passengers>
  </flight>
  <flight>
    <flight_number>FL003</flight_number>
    <origin>Tehran</origin>
    <destination>Paris</destination>
    <departure_date>2023-12-03</departure_date>
    <departure_time>14:00</departure_time>
    <arrival_date>2023-12-03</arrival_date>
    <arrival_time>21:30</arrival_time>
    <duration>7 hours 30 minutes</duration>
    <aircraft_type>Boeing 777</aircraft_type>
    <passengers>
      <passenger>
        <name>Emma Johnson</name>
        <age>27</age>
      </passenger>
      <passenger>
        <name>James Anderson</name>
        <age>45</age>
      </passenger>
    </passengers>
  </flight>
</airline>
'''

# Parse XML
root = ET.fromstring(xml_data)

# Find flights with destination "Paris"
paris_flights = []

for flight in root.findall('flight'):
    destination = flight.find('destination').text
    if destination.lower() == 'paris':
        paris_flights.append(flight)

# Print flight details
for flight in paris_flights:
    flight_number = flight.find('flight_number').text
    origin = flight.find('origin').text
    departure_date = flight.find('departure_date').text
    departure_time = flight.find('departure_time').text
    arrival_date = flight.find('arrival_date').text
    arrival_time = flight.find('arrival_time').text

    print(f"Flight Number: {flight_number}")
    print(f"Origin: {origin}")
    print(f"Departure Date: {departure_date}")
    print(f"Departure Time: {departure_time}")
    print(f"Arrival Date: {arrival_date}")
    print(f"Arrival Time: {arrival_time}")
    print("---------")
