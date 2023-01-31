from pathlib import Path
import csv

def Overhead():
    fp = Path.cwd()/"csv_reports"/"overheads-day-90.csv"
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)   

        overhead = []   
        for row in reader:
            overhead.append(row)

    category_base = ''
    overhead_base = ''
    for row in overhead:
        category = row[0]
        overhead =float(row[1])
        if overhead_base == '':
            overhead_base = overhead
        else:
            if overhead > overhead_base: 
                overhead_base = overhead
                category_base = category
            elif overhead < overhead_base:
                overhead_base = overhead_base    
                category = category_base   
    print(f'[HIGHEST OVERHEADS] {category}: {overhead_base}%')
Overhead()