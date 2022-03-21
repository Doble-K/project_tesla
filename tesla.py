#!/bin/bash/python
import ccxt
import time
import sys
# print (ccxt.exchanges)
# print(dir(ccxt.coinex()))


# print('python', sys.version)
# print('CCXT Version:', ccxt.__version__)
exchange = ccxt.coinex({
    'apiKey': 'XXX',
    'secret': 'XXX',
})

total_balance = exchange.fetch_balance()

total_coins_wallet = len(
    [coin for coin, balance in total_balance['total'].items() if balance > 0])

info = total_balance['info']
total = total_balance['total']
code = info['code']
data = info['data']
used = total_balance['used']
free = total_balance['free']
message = info['message']


print("")

# print ("Exchange: " + exchange)
# print("Pick first Coin:   ", end="")
# coin1 = str.upper(input())
# print("Pick second Coin:  ", end="")
# coin2 = str.upper(input())

exchange = "CoinEx"
# coin1 = 'BTC'
coin1 = 'BCH'
# coin1 = 'RTM'
# coin1 = 'TRX'
# coin2 = 'USDT'
coin2 = 'BTC'
pair = coin1 + '/' + coin2

for x in range(3):
    print(f" ---- {x} ---")
    time.sleep(0.9)
    limit = 10  # valor de no se que
    precio = ccxt.coinex().fetch_order_book(pair, limit)
# precio guardamos en variable,
# funcion de la api que trae los datos del par consultado

print("-----------")
print("Exchange: " + exchange)
print("-----------")
print("Moneda: " + pair)
print("-----------")

bids = precio['bids']
# guardamos los precios de compra
bajo = bids[0]
# guardo el precio mas alto de compra
volumenB = str(bajo[1]) + " " + coin1
# guardo el volumen junto a la moneda

print("Precio Compra: " + str(bajo[0]) + " " + coin2)
print("Volumen: " + volumenB)
print("-----------")

asks = precio['asks']
alto = asks[0]
volumenA = str(alto[1]) + " " + coin1

print("Precio Venta:  " + str(alto[0]) + " " + coin2)
print("Volumen: " + volumenA)
print("-----------")
# datetime = precio['datetime']
# print ("Hora: " + datetime)
# print ("-----------")
# print ("-----------")
# print ("-----------")

# for x in range(total_coins_wallet):
try:
    if coin1 in data and coin2 in data:
        print("If, coin1: ", coin1)
        print("If, data[coin1]", data[coin1])
        print("If, coin2: ", coin2)
        print("If, data[coin2]", data[coin2])
        print("print: 1")
        sys.exit()
    else:
        if coin1 in data and coin2 not in data:
            print("If, coin1: ", coin1)
            print("If, data[coin1]", data[coin1])
            print("print: 2")
            sys.exit()
        else:
            if coin1 not in data and coin2 in data:
                print("If, coin2: ", coin2)
                print("If, data[coin2]", data[coin2])
                print("print: 3")
                sys.exit()
            else:
                print(f"No hay Balance de {coin1} y {coin2}")
except KeyError:
    print("Error")
    sys.exit()
# Usamos un Try Except, porque tira error con if, al no econtrar la Moneda
# Si no esta en el diccionario.

# print("If, coin1: ", coin1)
# print("If, data[coin1]", data[coin1])
