import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

# App title
st.title("📈 Stock Price Viewer with Moving Averages")

# Sidebar inputs
st.sidebar.header("Configuration")

# Ticker input
ticker = st.sidebar.text_input("Enter Stock Ticker", value="AAPL")

# Date range picker (default: last 4 years)
start_date = st.sidebar.date_input("Start Date", date(2020, 1, 1))
end_date = st.sidebar.date_input("End Date", date(2024, 1, 1))

# Refresh button
refresh = st.sidebar.button("🔄 Refresh Data")

# Cache function with 5-min TTL
@st.cache_data(ttl=300)
def get_data(ticker, start_date, end_date):
    return yf.download(ticker, start=start_date, end=end_date)

# Clear cache if refresh clicked
if refresh:
    st.cache_data.clear()

# Load data
df = get_data(ticker, start_date, end_date)

# Validate data
if df.empty:
    st.error("⚠ Failed to load data. Possible reasons:\n- Invalid ticker\n- API rate limit reached. Try again later.")
else:
    # Calculate moving averages
    df['MA_20'] = df['Close'].rolling(window=20).mean()
    df['MA_50'] = df['Close'].rolling(window=50).mean()
    df['MA_100'] = df['Close'].rolling(window=100).mean()

    # Show data in expandable section
    with st.expander("📄 Show Raw Data"):
        st.dataframe(df)

    # Plot chart
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df['Close'], label='Close Price', color='blue')
    ax.plot(df['MA_20'], label='20-day MA', color='green')
    ax.plot(df['MA_50'], label='50-day MA', color='orange')
    ax.plot(df['MA_100'], label='100-day MA_]()
