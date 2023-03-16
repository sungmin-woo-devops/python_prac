class Stock:
    def __init__(self, name, ticker, per, pbr, divd):
        self.name = name
        self.ticker = ticker
        self.per = per
        self.pbr = pbr
        self.divd = divd
    
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


삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
print(삼성.get_name())
print(삼성.get_ticker())
print(삼성.get_per())
print(삼성.get_pbr())
print(삼성.get_divdend())
