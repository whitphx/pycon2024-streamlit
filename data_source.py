from datetime import datetime
import random


def get_stock_data(ticker=None):
    """Returns a simulated stock price."""
    timestamp = datetime.now()
    price = random.uniform(10, 30)  # Simulate price variation around 100
    return timestamp, price
