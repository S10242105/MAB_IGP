from pathlib import Path
import csv

fp = Path.cwd()/"csv_reports"/"overheads-day-90.csv"            
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    
    category = []
    overhead = []

    for row in reader:
        category.append(row[0])
        overhead.append(float(row[1]))

a = 0
b = 1

for i in overhead:
    while b < 11:
        if overhead[a] > overhead[b]:
            b += 1
            print(category[a])
        elif overhead[a] < overhead[b]:
            a=b
            b += 1
            print(category[a])
            
print(f'{category[a]} is the highest overheads in "Overheads.csv"')