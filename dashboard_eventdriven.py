import streamlit as st
from collections import deque
from queue import Queue
from event_dispatcher import data_source

st.title("Data Streaming Dashboard (Event-driven)")

max_rows = 100
stock_data = deque(maxlen=max_rows)

chart = st.empty()

q = Queue()

def on_update(timestamp, price):
    q.put((timestamp, price))

data_source.subscribe(on_update)

while True:
    timestamp, price = q.get()

    stock_data.append((timestamp, price))

    timestamps, prices = zip(*stock_data)

    chart.line_chart({"timestamp": timestamps, "price": prices}, x="timestamp", y="price")
