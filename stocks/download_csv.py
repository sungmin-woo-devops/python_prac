import yfinance as yf

df = yf.download("005930.KS", "2021-01-01", "2023-03-20")
df.to_csv("./stocks/삼성전자.csv")
df.head()