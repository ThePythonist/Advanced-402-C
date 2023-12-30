import csv


# ---------------- Working with DicReader and DictWriter ----------------

def write_csv_data(filename, data):
    fields = data[0].keys()

    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)


students = [
    {'Name': 'John Doe', 'Age': 20, 'Grade': 'A'},
    {'Name': 'Jane Smith', 'Age': 22, 'Grade': 'B'},
    {'Name': 'Michael Johnson', 'Age': 21, 'Grade': 'A'}
]

write_csv_data('students.csv', students)
