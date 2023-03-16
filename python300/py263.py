class Stock:
    def __init__(self, name, ticker):
        self.name = name
        self.ticker = ticker

    def set_name(self, name):
        self.name = name
    
a = Stock(None, None)
a.set_name("삼성전자")
print(a)
print(a.name)
print(a.ticker)
