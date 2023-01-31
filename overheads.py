from pathlib import Path
import csv

def FindMaxOverhead():
    fp = Path.cwd()/"csv_reports"/"overheads-day-90.csv" 
   
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)    
        overheadcsv = []   
    
        for row in reader:
            overheadcsv.append(row)
    
    filepath = Path.cwd()/"summary_report.txt"  
    with filepath.open(mode = "w", encoding = "UTF-8") as file:    
        maxOverhead = float(overheadcsv[0][1])  
        
        for row in overheadcsv:
            category = row[0]  
            overhead = float(row[1])   
            if overhead > maxOverhead:  
                maxOverhead = overhead 
       
        for row in overheadcsv:
            category = row[0]   
            overhead = float(row[1])    
            if overhead == maxOverhead:
                file.write(f'[HIGHEST OVERHEADS] {category}: {overhead}%\n')    