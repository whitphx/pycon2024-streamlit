import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import random
from collections import deque
from datetime import datetime

# Initialize the Dash app
app = dash.Dash(__name__)

# Simulate real-time stock price data for a single ticker
def get_stock_data():
    """Returns a simulated stock price."""
    timestamp = datetime.now()
    price = random.uniform(10, 30)  # Simulate price variation between 10 and 30
    return timestamp, price

# Initialize deque to store the latest 100 rows of data
max_rows = 100
stock_data = deque(maxlen=max_rows)

# Initialize with some starting data
for _ in range(max_rows):
    stock_data.append(get_stock_data())

# Define the layout of the app
app.layout = html.Div([
    html.H1("Real-Time Stock Price Dashboard"),
    dcc.Graph(id='live-graph'),
    dcc.Interval(
        id='interval-component',
        interval=10,  # Update every 0.01 seconds (10 milliseconds)
        n_intervals=0
    )
])

# Define the callback to update the graph
@app.callback(
    Output('live-graph', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_graph(n):
    # Update stock prices
    timestamp, price = get_stock_data()
    stock_data.append((timestamp, price))

    # Unpack the deque into two lists: timestamps and prices
    timestamps, prices = zip(*stock_data)

    # Create the Plotly figure
    fig = go.Figure(
        data=[go.Scatter(x=list(timestamps), y=list(prices), mode='lines')],
        layout=go.Layout(
            title="Stock Price Over Time",
            xaxis_title="Time",
            yaxis_title="Price",
            xaxis=dict(range=[min(timestamps), max(timestamps)]),
            yaxis=dict(range=[min(prices) - 5, max(prices) + 5]),
        )
    )

    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
