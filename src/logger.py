from datetime import datetime, date
import csv
import sys

def csvWrite(operation, amount, profit):
    now = datetime.now()
    today = date.today()

    with open('./logs/transactions.csv','a',newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([operation, amount, profit, today, now.strftime("%H:%M:%S")])
        csv_file.close()

def writeParams(invested, buyPrice, coinPrice, coinUp, coinDown):
    with open('./logs/log.txt', 'w') as f:
        sys.stdout = f 
        print(invested)
        print(buyPrice)
        print(coinPrice)
        print(coinUp)
        print(coinDown)
        f.close()
