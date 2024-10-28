import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import pandas as pd
import base64
import io

# Initialize the Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Upload and Visualize CSV Data with Dash"),

    # File upload component that accepts only CSV files
    dcc.Upload(
        id='upload-data',
        children=html.Button('Upload CSV'),
        accept='.csv',  # Accept only CSV files
        multiple=False
    ),

    # Placeholders for the data preview and chart
    html.Div(id='output-data-upload'),
    dcc.Graph(id='data-graph')
])

# Callback to parse the uploaded CSV and update the output
@app.callback(
    [Output('output-data-upload', 'children'), Output('data-graph', 'figure')],
    [Input('upload-data', 'contents')],
    [State('upload-data', 'filename')]
)
def update_output(contents, filename):
    if contents is None:
        return None, {}

    # Decode and parse the file
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))

    # Ensure the columns for Date and Stock Price exist
    if 'Date' not in df.columns or 'Stock Price' not in df.columns:
        return html.Div(["Error: CSV must contain 'Date' and 'Stock Price' columns."]), {}

    # Convert Date column to datetime for accurate plotting
    df['Date'] = pd.to_datetime(df['Date'])

    # Data preview
    preview = html.Div([
        html.H5(f"Uploaded File: {filename}"),
        html.P("Data Preview:"),
        html.Table([
            html.Tr([html.Th(col) for col in df.columns])] +
            [html.Tr([html.Td(df.iloc[i][col]) for col in df.columns]) for i in range(min(len(df), 5))])
    ])

    # Define the figure with specified columns
    fig = {
        'data': [{
            'x': df['Date'],
            'y': df['Stock Price'],
            'type': 'line',
            'name': 'Stock Price'
        }],
        'layout': {
            'title': 'Uploaded Data Visualization',
            'xaxis': {'title': 'Date'},
            'yaxis': {'title': 'Stock Price'}
        }
    }

    return preview, fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
