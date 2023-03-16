class Stock:
    def __init__(self, name, ticker):
        self.name = name
        self.ticker = ticker

삼성 = Stock("삼성전자", "005930")
print(삼성)
print(삼성.name)
print(삼성.ticker)
