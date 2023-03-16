class Stock:
    def __init__(self, name, ticker):
        self.name = name
        self.ticker = ticker

    def set_code(self, ticker):
        self.ticker = ticker

a = Stock(None, None)
a.set_code("005930")

print(a)
print(a.name)
print(a.ticker)
