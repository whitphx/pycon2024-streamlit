import streamlit as st
import time
from collections import deque
from data_source import get_stock_data

st.title("Data Streaming Dashboard")

max_rows = 100
stock_data = deque(maxlen=max_rows)

chart = st.empty()

while True:
    timestamp, price = get_stock_data()

    stock_data.append((timestamp, price))

    timestamps, prices = zip(*stock_data)

    chart.line_chart({"timestamp": timestamps, "price": prices}, x="timestamp", y="price")

    time.sleep(0.01)
