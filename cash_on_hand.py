from pathlib import Path
import csv

def CashOnHand():
    """
    - Function to calculate the difference in Cash-On-Hand between one day to the next.
    """
    fp = Path.cwd()/"project_group"/"csv_reports"/"cash-on-hand-usd.csv"    # Path to csv file
    # Read data from csv
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)    # Skip csv header
        cash_on_hand = []   # Initialise variable to store data from csv
        # Read all data into cash_on_hand
        for row in reader:
            cash_on_hand.append(row)

    filepath = Path.cwd()/"summary_report.txt"  # Path to output file
    with filepath.open(mode = "a", encoding = "UTF-8") as file:   # Append into output file
        prevCOH = ''    # Variable to store previous cash-on-hand. Initialise as empty.
        cash_deficit = 0    # Stores total number of cash deficits
        # Iterate over each row
        for row in cash_on_hand:
            day = float(row[0])     # Day as a float
            cash = float(row[1])    # Cash-on-hand as a float
            if prevCOH == '':       # If empty, it means prevCOH does not yet contain previous cash-on-hand
                prevCOH = cash      # Store first cash-on-hand into prevCOH for comparison
            else:                   # prevCOH already contains previous cash-on-hand
                if cash < prevCOH:    # Checks if current day cash-on-hand is lower than previous
                    file.write(f'[CASH DEFICIT] DAY: {day}, AMOUNT: USD{prevCOH-cash}\n')   # Write in output file
                    cash_deficit += 1   # Increment cash_deficit counter
                prevCOH = cash
        if cash_deficit == 0:       # If no cash_deficit, then it is all surplus (or same)
            file.write(f'[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY')  # Write in output file
