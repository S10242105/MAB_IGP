from pathlib import Path
import csv

def FindMaxOverhead():
    """
    - Function to find the highest overhead category.
    """
    fp = Path.cwd()/"csv_reports"/"overheads-day-90.csv"    # Path to csv input file
    # Read data from csv
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)    # Skip csv header
        overheadcsv = []    # Initialise variable to store data from csv
        # Read all data into overheadcsv
        for row in reader:
            overheadcsv.append(row)
    
    filepath = Path.cwd()/"summary_report.txt"  # Path to output file
    with filepath.open(mode = "w", encoding = "UTF-8") as file:     # Open output file for write
        maxOverhead = float(overheadcsv[0][1])  # Assign the first overhead to maxOverhead 
        # Iterate over each row to find the largest overhead
        for row in overheadcsv:
            category = row[0]   # Category
            overhead = float(row[1])    # Overhead as a float
            if overhead > maxOverhead:  # Compares if overhead is larger than stored maxOverhead value
                maxOverhead = overhead  # Store larger overhead value as maxOverhead
        # Second iteration, find all accounts with maximum overhead and write to output file
        for row in overheadcsv:
            category = row[0]   
            overhead = float(row[1])    
            if overhead == maxOverhead: # Checks if the overhead value is the highest
                file.write(f'[HIGHEST OVERHEADS] {category}: {overhead}%\n')    # Write in output file