import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State, ALL

# Initialize the Dash app
app = dash.Dash(__name__, suppress_callback_exceptions=True)

# App layout
app.layout = html.Div([
    html.H1("Budget Allocator"),

    # Input for total budget
    html.Label("Total Budget ($):"),
    dcc.Input(id="total-budget", type="number", value=5000, min=1000, step=500, style={"margin-bottom": "20px"}),

    # Input for number of categories
    html.Label("Number of Categories:"),
    dcc.Input(id="num-categories", type="number", value=3, min=1, style={"margin-bottom": "20px"}),

    # Placeholder for dynamically generated sliders
    html.Div(id="sliders-container", style={"margin-bottom": "20px"}),

    # Summary of allocation
    html.H3("Allocation Summary"),
    html.Div(id="summary-output"),
])

# Callback to generate sliders dynamically based on the number of categories
@app.callback(
    Output("sliders-container", "children"),
    [Input("num-categories", "value"), Input("total-budget", "value")]
)
def create_sliders(num_categories, total_budget):
    sliders = []
    for i in range(num_categories):
        slider = html.Div([
            html.Label(f"Category {i + 1} Allocation"),
            dcc.Slider(
                id={'type': 'category-slider', 'index': i},
                min=0, max=total_budget, value=total_budget // num_categories,
                marks={0: "0", total_budget: str(total_budget)}
            )
        ], style={"margin-bottom": "20px"})
        sliders.append(slider)
    return sliders

# Callback to update allocation summary based on slider values
@app.callback(
    Output("summary-output", "children"),
    Input("total-budget", "value"),
    Input({'type': 'category-slider', 'index': ALL}, 'value')
)
def update_summary(total_budget, allocations):
    total_allocated = sum(allocations)
    remaining_budget = total_budget - total_allocated

    summary = [
        html.P(f"Total Allocated: ${total_allocated}"),
        html.P(f"Remaining Budget: ${remaining_budget}")
    ]

    if total_allocated > total_budget:
        summary.append(html.Div("You have exceeded the total budget!", style={"color": "red"}))
    elif remaining_budget < total_budget * 0.1:
        summary.append(html.Div("Warning: You are nearing your total budget.", style={"color": "orange"}))
    else:
        summary.append(html.Div("You are within the budget.", style={"color": "green"}))

    return summary

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
