import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import random
from collections import deque
from datetime import datetime

# Initialize the Dash app
app = dash.Dash(__name__)

# Constants for grid size
NUM_COLUMNS = 5
NUM_ROWS = 30
MAX_TICKERS = NUM_COLUMNS * NUM_ROWS
MAX_DATA_POINTS = 100  # Maximum number of data points to keep

# Simulate real-time stock price data for multiple tickers
def get_stock_data(ticker):
    """Returns a simulated stock price for a given ticker."""
    timestamp = datetime.now()
    price = random.uniform(10, 30)  # Simulate price variation between 10 and 30
    return timestamp, price

# Initialize deque for each ticker to store the latest 100 rows of data
stock_data = {f"TICKER{i+1}": deque(maxlen=MAX_DATA_POINTS) for i in range(MAX_TICKERS)}

# Pre-populate initial data for each ticker
for ticker in stock_data:
    for _ in range(MAX_DATA_POINTS):
        stock_data[ticker].append(get_stock_data(ticker))

# Define the layout of the app with 5x30 grid of real-time charts
app.layout = html.Div([
    html.H1("5x30 Real-Time Stock Price Dashboard"),
    html.Div([
        html.Div([
            dcc.Graph(id=f'graph-{ticker}')
        ], style={'width': '19%', 'display': 'inline-block'})  # Adjusting column width to fit 5 columns
        for ticker in stock_data
    ]),
    dcc.Interval(
        id='interval-component',
        interval=10,  # Update every 0.01 seconds
        n_intervals=0
    )
])

# Define the callback to update all graphs dynamically
@app.callback(
    [Output(f'graph-TICKER{i+1}', 'figure') for i in range(MAX_TICKERS)],
    [Input('interval-component', 'n_intervals')]
)
def update_graphs(n):
    figures = []
    for i in range(MAX_TICKERS):
        ticker = f"TICKER{i+1}"
        timestamp, price = get_stock_data(ticker)
        stock_data[ticker].append((timestamp, price))

        # Unpack the deque into two lists: timestamps and prices
        timestamps, prices = zip(*stock_data[ticker])

        # Create the Plotly figure
        fig = go.Figure(
            data=[go.Scatter(x=list(timestamps), y=list(prices), mode='lines')],
            layout=go.Layout(
                title=ticker,
                xaxis_title="Time",
                yaxis_title="Price",
                xaxis=dict(range=[min(timestamps), max(timestamps)]),
                yaxis=dict(range=[min(prices) - 5, max(prices) + 5]),
                height=250  # Adjust the height to fit the grid
            )
        )

        figures.append(fig)

    return figures

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
