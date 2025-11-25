import csv

# Change this to your CSV file name
filename = "examples.csv"

with open(filename, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)

    count = 0
    for row in reader:
        print(row)      # print the entire row as a Python list
        count += 1
        if count == 10: # stop after 10 rows
            break
