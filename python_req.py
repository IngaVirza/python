import requests
import time

url = 'https://api.binance.com/api/v3/ticker/price'

response = requests.get(url, params={'symbol': 'BTCUSDT'})

content = response.content

price = response.json()
print(price)
print(type(price))


#{'symbol': 'BTCUSDT', 'price': '66451.42000000'}
#<class 'dict'>

bitcoin_prices = []
for i in range(30):
    response = requests.get(url, params={'symbol': 'BTCUSDT'})
    price = float(response.json()['price'])
    bitcoin_prices.append(price)
    time.sleep(1)

    print(bitcoin_prices)
    print(len(bitcoin_prices))

#[66451.42]
#1
#[66451.42, 66450.97]
#2
#[66451.42, 66450.97, 66449.88]
#3
#...

