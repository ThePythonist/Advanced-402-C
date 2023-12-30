import csv

filename = 'data.csv'

data1 = [
    ['Name', 'Age', 'City'],
    ['John', '25', 'New York'],
    ['Alice', '30', 'London'],
    ['Bob', '35', 'Paris']
]

data2 = [
    ['Mike', '40', 'Berlin'],
    ['Emily', '28', 'Tokyo']
]


def write(data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print(f'{filename} has been created successfully.')


def read(file):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            print(row)


def add(data):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print(f'{filename} has been updated successfully.')

# write(data1)
# add(data2)
read(filename)
