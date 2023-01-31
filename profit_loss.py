from pathlib import Path
import csv

def ProfitLoss():
    """
    - Function calculates the difference in Net Profit if the net profit on the current day is lower than the previous.
    """
    fp = Path.cwd()/"csv_reports"/"profit-and-loss-usd.csv"     # Path to csv input file
    # Read data from csv
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)    # Skip csv header
        profit_loss = []    # Initialise to store data from csv
        # Read all data into profit_loss
        for row in reader:
            profit_loss.append(row)

    filepath = Path.cwd()/"summary_report.txt"  # Path to output file
    with filepath.open(mode = "a", encoding = "UTF-8") as file:     # Append into output file
        prevPL = ''     # Store previous net profit for comparison. Initialise as empty string.
        profit_deficit = 0      # Stores total number of net profit deficits
        # Iterate over each row
        for row in profit_loss:
            day = float(row[0])     # Day as a float
            net_profit = float(row[4])  # net profit as a float
            if prevPL == '':            # prevPL does not yet contain previous net profit
                prevPL = net_profit     # Store first net profit into prevPL for comparison
            else:                       # prevPL already contains previous net profit
                if net_profit < prevPL:     # Checks if current day net profit is lower than previous
                    file.write(f'[NET PROFIT DEFICIT] DAY: {day}, AMOUNT: USD{prevPL-net_profit}\n')    # Write in output file
                    profit_deficit += 1     # Increment profit_deficit counter
                prevPL = net_profit
        if profit_deficit == 0:     # If no profit_deficit, then it is all surplus (or same)
            file.write(f'[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY')  # Write in output file