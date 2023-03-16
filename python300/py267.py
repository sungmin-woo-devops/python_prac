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


삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
