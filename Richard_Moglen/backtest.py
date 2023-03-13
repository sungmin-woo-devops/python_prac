import pandas
import numpy as np
import yfinance as yf
import datetime as dt
from pandas_datareader import data as pdr

yf.pdr_override()

stock = input("Enter a stock ticker symbol: ")
print(stock)

start_year = 2019
start_month = 1
start_day = 1

start = dt.date(start_year, start_month, start_day)
now = dt.datetime.now()

df = pdr.get_data_yahoo(stock, start, now)

ma = 50
smaString = "Sma_" + str(ma)

df[smaString] = df.iloc[:,4].rolling(window=ma).mean()
# smaString 열 생성
# 윈도우 사이즈가 ma(=50)인 adjust close price를 
# 이용한 이동평균열 생성

df = df.iloc[ma:]
# 처음 50개의 데이터는 50일 이평선 데이터가 없으므로(NaN) 제거

#for i in df.index:
#    print(i)
# 각 dataframe의 index row 출력
# -> date를 이용하여 데이터 구분 가능

#for i in df.index:
#    # print(df.iloc[:,4][1]) # method 1
#    # print(df["Adj Close"][i])
# adjusted close value 출력

# for i in df.index:
#    print(df[smaString][i])
# MA50 출력

numH = 0
numL = 0

for i in df.index:
    if(df["Adj Close"][i] > df[smaString][i]):
        print("The Close is higher")
        numH += 1
    elif(df["Adj Close"][i] == df[smaString][i]):
        print("The Close is equal to SMA50")
    else:
        print("The Close is lower")
        numL += 1

print(f"numH: {numH}")
print(f"numL: {numL}")

