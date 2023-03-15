icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}

price_sum = 0
for price in list(icecream.values()):
    price_sum = price_sum + price

print(price_sum)
