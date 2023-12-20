import xml.etree.ElementTree as ET
import xmltodict

tree = ET.parse("flights.xml")

xml_data = tree.getroot()
# print(xml_data)

xml_string = ET.tostring(xml_data, encoding='utf8', method='xml')
# print(xml_string)

xml_dict = xmltodict.parse(xml_string)
print(xml_dict)
