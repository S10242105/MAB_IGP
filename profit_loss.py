from pathlib import Path
import csv

fp = Path.cwd()/"csv_reports"/"profit-and-loss-usd.csv"
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    day = []
    net_profit = []

    for row in reader:
        day.append(row[0])
        net_profit.append(float(row[4]))

a = 0
b = 1

for i in net_profit:
    while b < 11:
        if net_profit[a] > net_profit[b]:
            difference = net_profit[a] - net_profit[b]
            print(f"[NET PROFIT DEFICIT] DAY: {b}, AMOUNT: USD{difference}")
            a += 1
            b += 1
        elif net_profit[a] < net_profit[b]:
            print(f'[NET PROFIT SURPLUS] NET PROFIT ON DAY {day[b]} IS HIGHER THAN DAY {day[a]}')
            a += 1
            b += 1