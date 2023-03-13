import pandas_datareader as web
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

start = dt.datetime(2018, 1, 1)
end = dt.datetime.now()

tickers = ["NVDA", "MSFT", "TSLA", "AAPL", "CCL, BA"]
colnames = []

for ticker in tickers:
    data = web.DataReader(ticker, "yahoo", start, end)
    if len(colnames) == 0:
        combined = data[['Adj Close']].copy()
        colnames.append(ticker)
        combined.columns = colnames
    else:
        combined = combined.join(data['Adj Close'])
        colnames.append(ticker)
        combined.columns = colnames

print(combined)
# ---------------------------------------------------------
# https://www.youtube.com/watch?v=Jfo22-qB4UI
