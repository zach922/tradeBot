import time
import config
from binance.client import Client
from binance.enums import *
from binance.websockets import BinanceSocketManager

SYMBOL = 'BTCUSDT'
QUANTITY = '0.0001'
PERCENT = 0.01

def GetPrice(symbol='BTCUSDT'):
    # def proc(msg):
    #     print(str(msg['w']))
    #     return float(msg['w'])
        
        
        
    
    # bm = BinanceSocketManager(client)
    # conn_key = bm.start_symbol_ticker_socket(symbol, proc)

    # bm.start() 


    price = client.get_all_tickers()
    amount = price[6]['price']
    print(price[6]['price'])
    return float()

def order(symbol, quantity, side, order_type=ORDER_TYPE_MARKET):
    try: 
        order = client.create_order(symbol=symbol, side = side, type=order_type, quantity = quantity)
        print ("%s order successful" % (side) )
    except Exception as e:
        print ("%s order failed: %s" % (side, e) )
        return False
    return True


print('Opening client')
api_key = config.API_KEY
api_secret = config.API_SECRET

client = Client(api_key, api_secret, tld='us')

invested = False
coinPrice = GetPrice()
coinUp = coinPrice*(1.0+PERCENT)    
coinDown = coinPrice*(1.0-PERCENT)

try:
    while(True):
        coinPrice = GetPrice()
        if (not invested and coinPrice >= coinUp):
            if(order(SYMBOL, QUANTITY, SIDE_BUY)):
                invested = True
            coinDown = coinPrice*(1.0-PERCENT)  
        elif (invested and coinPrice <= coinDown):
            if(order(SYMBOL, QUANTITY, SIDE_SELL)):
                invested = False
            coinUp = coinPrice*(1.0+PERCENT)
        time.sleep(5)

except KeyboardInterrupt:
    print("Exiting client")

