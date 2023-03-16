class Stock:
    def __init__(self, name, ticker):
        self.name = name
        self.ticker = ticker

    def get_name(self):
        return self.name

    def get_ticker(self):
        return self.ticker

삼성 = Stock("삼성전자", "005930")

print(삼성)
print(삼성.get_name())
print(삼성.get_ticker())
