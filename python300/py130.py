import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

# 방법 1
delta = float(btc['max_price']) - float(btc['min_price'])
if float(btc['max_price']) < float(btc['opening_price']) + delta:
    print("상승장")
else:
    print("하락장")

# 방법 2
변동폭 = float(btc['max_price']) - float(btc['min_price'])
시가 = float(btc['opening_price'])
최고가 = float(btc['max_price'])

if (시가 + 변동폭) > 최고가:
    print("상승장")
else:
    print("하락장")
