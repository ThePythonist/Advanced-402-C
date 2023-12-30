import csv

# ---------------- Working with DictReader and DictWriter ----------------

# with open('data.csv', 'r') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         # Access values using column names
#         print(row)

with open('data.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Name', 'Age'])
    writer.writeheader()  # Write the header row
    writer.writerow({'Age': '23', 'Name': 'Ali'})  # Write a row
    writer.writerow({'Name': 'Farzad', 'Age': '14'})  # Write a row
