from pathlib import Path
import csv

def CashOnHand():
    fp = Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"    

    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)   
        cash_on_hand = []  
     
        for row in reader:
            cash_on_hand.append(row)

    filepath = Path.cwd()/"summary_report.txt" 
    with filepath.open(mode = "a", encoding = "UTF-8") as file:   
        prevCOH = ''    
        cash_deficit = 0   
      
        for row in cash_on_hand:
            day = float(row[0])     
            cash = float(row[1])    
            if prevCOH == '':       
                prevCOH = cash     
            else:                   
                if cash < prevCOH:   
                    file.write(f'[CASH DEFICIT] DAY: {day}, AMOUNT: USD{prevCOH-cash}\n')  
                    cash_deficit += 1 
                prevCOH = cash
        if cash_deficit == 0:      
            file.write(f'[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY')  