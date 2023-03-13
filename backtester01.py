import backtrader as bt

class MyStrategy(bt.Strategy):
    def next(self):
        pass #Do Something

# instantiate Cerebro engine
cerebro = bt.Cerebro()

# Add Strategy to Cerebro
cerebrro.addstrategy(MyStrategy)

# Run Cerebro Engine
cerebro.run()
