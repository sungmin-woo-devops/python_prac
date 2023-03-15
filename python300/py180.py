low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

# 방법 1
volatility = [i - j for i, j in zip(low_prices, high_prices)]
print(volatility)

# 방법 2
for i in range(len(low_prices)):
    volatility.append(high_prices[i] - low_prices[i])
