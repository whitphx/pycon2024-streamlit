import random
import threading
import time
from datetime import datetime

class MockEventDispatcher:
    def __init__(self, interval=0.5):
        self.callbacks = []
        self.interval = interval
        self.running = False

    def subscribe(self, callback):
        """Subscribe a new listener (callback function)."""
        self.callbacks.append(callback)

    def start(self):
        """Start the event dispatcher in a separate thread."""
        if not self.running:
            self.running = True
            thread = threading.Thread(target=self._run, daemon=True)
            thread.start()

    def stop(self):
        """Stop the event dispatcher."""
        self.running = False

    def _run(self):
        """Run the dispatcher to generate and dispatch mock data."""
        while self.running:
            time.sleep(random.uniform(0.01, self.interval))  # Simulate event timing
            timestamp, price = self._get_stock_data()
            # Notify all subscribers (callbacks) with mock stock data
            for callback in self.callbacks:
                callback(timestamp, price)

    def _get_stock_data(self):
        """Simulate generating a single stock price event."""
        timestamp = datetime.now()
        price = random.uniform(10, 30)  # Simulate price variation between 10 and 30
        return timestamp, price

# Instantiate the event dispatcher as a module-level object
data_source = MockEventDispatcher(interval=0.5)
data_source.start()
