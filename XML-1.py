import xmltodict
from pprint import pprint

xml_data = '''
<bookstore>
    <book>
        <title>Harry Potter and the Philosopher's Stone</title>
        <author>J.K. Rowling</author>
        <genre>Fantasy</genre>
        <price>19.99</price>
    </book>
    <book>
        <title>The Great Gatsby</title>
        <author>F. Scott Fitzgerald</author>
        <genre>Classic</genre>
        <price>12.99</price>
    </book>
    <book>
        <title>Blind Owl</title>
        <author>Sadegh Hedayat</author>
        <genre>Fiction</genre>
        <price>15.99</price>
    </book>
</bookstore>
'''

xml_dict = xmltodict.parse(xml_data)
bookstore = xml_dict["bookstore"]
books = bookstore["book"]

for book in books:
    print(book["title"],":",book["price"])
