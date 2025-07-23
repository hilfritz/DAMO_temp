import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ticker = 'AAPL'
df = yf.download(ticker, start='2020-01-01', end='2024-01-01')

# plotting time series data
#plt.figure(figsize=(10, 5))
#plt.plot(df['Close'], label='Close Price')
#plt.title(f'{ticker} Stock Price')
#plt.xlabel('Date')
#plt.ylabel('Price (USD)')
#plt.legend()
#plt.show()


#MOVING AVERAGE CALCULATION
#df_clean = df.dropna().copy
df['MA_50'] = df['Close'].rolling(window=50).mean()
df['MA_100'] = df['Close'].rolling(window=100).mean()
df['MA_20'] = df['Close'].rolling(window=20).mean()
#df.head(5)



# plotting time series data
plt.figure(figsize=(10, 5))
plt.plot(df['MA_50'], label='50 day moving average')
plt.plot(df['MA_20'], label='20 day moving average')
plt.plot(df['MA_100'], label='20 day moving average')
plt.title(f'{ticker} Stock Price')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.show()
