import streamlit as st
from collections import deque
from queue import Queue
from event_dispatcher import data_source

# Set up the title of the app
st.title("Real-Time Stock Price Dashboard (Event listener-based)")

# Initialize deque to store the latest 100 rows of data
max_rows = 100
stock_data = deque(maxlen=max_rows)

# Set up the chart placeholder
chart = st.empty()

q = Queue()

def on_update(timestamp, price):
    q.put((timestamp, price))

data_source.subscribe(on_update)

while True:
    timestamp, price = q.get()

    stock_data.append((timestamp, price))
    # Unpack the deque into two lists: timestamps and prices
    timestamps, prices = zip(*stock_data)
    # Update the Streamlit chart
    chart.line_chart({"timestamp": timestamps, "price": prices}, x="timestamp", y="price")
