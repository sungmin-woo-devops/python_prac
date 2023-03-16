class Stock:
    def __init__(self, name, ticker, per, pbr, divd):
        self.name = name
        self.ticker = ticker
        self.per = per
        self.pbr = pbr
        self.divd = divd

    # getter
    def get_name(self):
        return self.name

    def get_ticker(self):
        return self.ticker
    
    def get_per(self):
        return self.per

    def get_pbr(self):
        return self.pbr

    def get_divdend(self):
        return self.divd

    # setter
    def set_name(self, name):
        self.name = name

    def set_ticker(self, ticker):
        self.ticker = ticker

    def set_per(self, per):
        self.per = per

    def set_pbr(self, pbr):
        self.pbr = pbr
    
    def set_dividend(self, divd):
        self.divd = divd


삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
현대 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

stocks = [삼성, 현대, LG전자]

for stock in stocks:
    print(f"{stock.get_name()}: {stock.get_per()}")
