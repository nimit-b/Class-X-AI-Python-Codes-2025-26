import csv
filename = 'examples.csv'
with open(filename, newline='', encoding = 'utf-8')as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
