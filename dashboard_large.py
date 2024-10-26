import streamlit as st
import time
from collections import deque
from data_source import get_stock_data

NUM_ROWS = 20
NUM_COLUMNS = 5
MAX_TICKERS = NUM_ROWS * NUM_COLUMNS
MAX_ROWS = 10  # Max rows to store in deque

st.title(f"Data Streaming Dashboard ({NUM_ROWS}x{NUM_COLUMNS})")

tickers = [f'TICKER{i+1}' for i in range(MAX_TICKERS)]

stock_data = {ticker: deque(maxlen=MAX_ROWS) for ticker in tickers}

rows = [st.columns(NUM_COLUMNS) for _ in range(NUM_ROWS)]
charts = {}
for i, ticker in enumerate(tickers):
    row = i // NUM_COLUMNS  # Determine the row for the chart
    col = i % NUM_COLUMNS   # Determine the column for the chart
    charts[ticker] = rows[row][col].empty()

while True:
    for ticker in tickers:
        timestamp, price = get_stock_data(ticker)

        stock_data[ticker].append((timestamp, price))

        timestamps, prices = zip(*stock_data[ticker])

        charts[ticker].line_chart({"timestamp": timestamps, "price": prices}, x="timestamp", y="price")

    # Simulate a delay for real-time effect
    time.sleep(0.01)
