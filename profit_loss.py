from pathlib import Path
import csv

def ProfitLoss():
    fp = Path.cwd()/"project_group"/"csv_reports"/"profit-and-loss-usd.csv"     

    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) 
        profit_loss = []   
        
        for row in reader:
            profit_loss.append(row)

    filepath = Path.cwd()/"summary_report.txt"  
    with filepath.open(mode = "a", encoding = "UTF-8") as file:   
        prevPL = ''   
        profit_deficit = 0    

        for row in profit_loss:
            day = float(row[0])    
            net_profit = float(row[4])  
            if prevPL == '':            
                prevPL = net_profit    
            else:                     
                if net_profit < prevPL:    
                    file.write(f'[NET PROFIT DEFICIT] DAY: {day}, AMOUNT: USD{prevPL-net_profit}\n')    
                    profit_deficit += 1    
                prevPL = net_profit
        if profit_deficit == 0:     
            file.write(f'[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY')  