import streamlit as st
import random
import time
from collections import deque
from datetime import datetime

# Constants to define the grid size
NUM_ROWS = 30
NUM_COLUMNS = 5
MAX_TICKERS = NUM_ROWS * NUM_COLUMNS
MAX_ROWS = 100  # Max rows to store in deque

# Title of the app
st.title(f"Real-Time Multi-Stock Dashboard ({NUM_ROWS}x{NUM_COLUMNS})")

# Simulate real-time stock price data for multiple tickers
def get_stock_data(ticker):
    """Returns a simulated stock price for a given ticker."""
    timestamp = datetime.now()
    price = random.uniform(10, 30)  # Simulate price variation
    return timestamp, price

# Create a list of tickers based on grid size (NUM_ROWS x NUM_COLUMNS)
tickers = [f'TICKER{i+1}' for i in range(MAX_TICKERS)]

# Initialize deque for each ticker to store the latest 100 rows of data
stock_data = {ticker: deque(maxlen=MAX_ROWS) for ticker in tickers}

# Create placeholders for the charts in the grid
rows = [st.columns(NUM_COLUMNS) for _ in range(NUM_ROWS)]
charts = {}
for i, ticker in enumerate(tickers):
    row = i // NUM_COLUMNS  # Determine the row for the chart
    col = i % NUM_COLUMNS   # Determine the column for the chart
    charts[ticker] = rows[row][col].empty()

# Infinite loop for real-time updates
while True:
    for ticker in tickers:
        # Get the latest stock price for each ticker
        timestamp, price = get_stock_data(ticker)

        # Append new data to the deque for this ticker
        stock_data[ticker].append((timestamp, price))

        # Unpack the deque into lists of timestamps and prices
        timestamps, prices = zip(*stock_data[ticker])

        # Update the chart for the current ticker
        charts[ticker].line_chart({"timestamp": timestamps, "price": prices}, x="timestamp", y="price")

    # Simulate a delay for real-time effect
    time.sleep(0.01)
