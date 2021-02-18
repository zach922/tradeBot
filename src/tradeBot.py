from binance.client import Client
import sys
import csv
import time
from datetime import datetime, date
import os


def csvWrite(operation, amount, profit):
    now = datetime.now()
    today = date.today()

    with open('./logs/transactions.csv','a',newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([operation, amount, profit, today, now.strftime("%H:%M:%S")])
        csv_file.close()

def GetPrice():
    price = client.get_all_tickers()
    #currency = price[11]['symbol']
    amount = price[11]['price']
    #print("Price for %s is: %s " % (currency, str(amount)))
    return float(amount)

def buyMax(currency):
    amount = 91.10
    print("Buying %s$USD worth of %s " % (str(amount), currency))
    return amount


def sellMax(currency):
    amount = 91.10
    print("Selling %sUSD worth of %s " % (str(amount), currency))
    return amount


api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')

print('Opening client')
client = Client(api_key, api_secret)

invested = False
coinPrice = GetPrice() #get-price api call
currency = "BTC"
amount = 0.0
buyPrice = 0.0
sellPrice = 0.0
profit = 0.0
percent = 0.01
coinUp = coinPrice*(1.0+percent)     # 2% up
coinDown = coinPrice*(1.0-percent)  # 2% down

with open('./logs/log.txt', 'r') as f:
    tmp = f.readline()
    if(tmp != ''):
        invested = bool(tmp)
        buyPrice = float(f.readline())
        coinPrice = float(f.readline()) #get-price api call
        coinUp = float(f.readline()) #buyPrice*(1.0+percent)     # 2% up
        coinDown = float(f.readline()) #buyPrice*(1.0-percent)  # 2% down
    f.close()

try:
    while(True):
        if (not invested and coinPrice >= coinUp):
            amount = buyMax(currency)
            invested = True
            buyPrice = coinPrice
            profit = buyPrice - sellPrice
            sellPrice = 0.0
            coinDown = coinPrice*0.98   # 2% down
            csvWrite("Buy", amount, profit)
        elif (invested and coinPrice <= coinDown):
            amount = sellMax(currency)
            invested = False
            sellPrice = coinPrice
            profit = buyPrice - sellPrice;
            buyPrice = 0.0
            coinUp = coinPrice*1.02     # 2% up
            csvWrite("Sell", amount, profit)

        time.sleep(1)
        coinPrice = GetPrice()
        os.system('cls' if os.name == 'nt' else 'clear')
        print("BuyPrice: %s\nPrice:    %s \nCoinUp:   %s \nCoinDown: %s \n" % (str(buyPrice), str(coinPrice), str(coinUp), str(coinDown)))
except:
    print("Exiting client after saving parameters. ")
    with open('./logs/log.txt', 'w') as f:
        sys.stdout = f 
        print(buyPrice)
        print(invested)
        print(coinPrice)
        print(coinUp)
        print(coinDown)
        f.close()
