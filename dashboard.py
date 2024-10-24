import streamlit as st
import random
import time
from collections import deque
from datetime import datetime

st.title("Real-Time Stock Price Dashboard")

def get_stock_data():
    """Returns a simulated stock price."""
    timestamp = datetime.now()
    price = random.uniform(10, 30)  # Simulate price variation around 100
    return timestamp, price

max_rows = 100
stock_data = deque(maxlen=max_rows)

chart = st.empty()

while True:
    timestamp, price = get_stock_data()

    stock_data.append((timestamp, price))

    timestamps, prices = zip(*stock_data)

    chart.line_chart({"timestamp": timestamps, "price": prices}, x="timestamp", y="price")

    time.sleep(0.01)
