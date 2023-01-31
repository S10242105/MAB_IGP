from pathlib import Path
import csv

fp = Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    day = []
    cash_on_hand = []

    for row in reader:
        day.append(row[0])
        cash_on_hand.append(float(row[1]))

a = 0
b = 1

for i in cash_on_hand:
    while b < 11:
        if cash_on_hand[a] > cash_on_hand[b]:
            difference = cash_on_hand[a] - cash_on_hand[b]
            print(f"[CASH DEFICIT] DAY: {day[b]}, AMOUNT: USD{difference}")
            a += 1
            b += 1
        elif cash_on_hand[a] < cash_on_hand[b]:
            print(f'[CASH SURPLUS] CASH ON DAY {day[b]} IS HIGHER THAN DAY {day[a]}')
            a += 1
            b += 1