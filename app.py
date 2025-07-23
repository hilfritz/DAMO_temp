import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# App title
st.title("Stock Price Viewer with Moving Averages")

# User input for ticker
ticker = st.text_input("Enter Stock Ticker", value="AAPL")

# Button to refresh data
refresh = st.button("Refresh Data")

@st.cache_data(ttl=300)  # Cache for 5 minutes
def get_data(ticker):
    return yf.download(ticker, start='2020-01-01', end='2024-01-01')

# Load data
if refresh:
    st.cache_data.clear()  # Clear cache when refresh button clicked

df = get_data(ticker)

# Check if data is available
if df.empty:
    st.error("Failed to load data (rate limit or invalid ticker). Try again later.")
else:
    # Calculate moving averages
    df['MA_50'] = df['Close'].rolling(window=50).mean()
    df['MA_100'] = df['Close'].rolling(window=100).mean()
    df['MA_20'] = df['Close'].rolling(window=20).mean()

    # Show raw data
    with st.expander("Show Raw Data"):
        st.dataframe(df)

    # Plotting
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df['Close'], label='Close Price', color='blue')
    ax.plot(df['MA_20'], label='20-day MA', color='green')
    ax.plot(df['MA_50'], label='50-day MA', color='orange')
    ax.plot(df['MA_100'], label='100-day MA', color='red')
    ax.set_title(f"{ticker} Stock Price & Moving Averages")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price (USD)")
    ax.legend()
    st.pyplot(fig)
