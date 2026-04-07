import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load the formatted sales data
df = pd.read_csv("formatted_output.csv")
df["date"] = pd.to_datetime(df["date"])

# Initialize the Dash app
app = Dash(__name__)
app.title = "Pink Morsel Sales Visualiser"

# App layout
app.layout = html.Div(
    style={"fontFamily": "Arial, sans-serif", "textAlign": "center", "margin": "20px"},
    children=[
        html.H1("Pink Morsel Sales Dashboard", style={"color": "#D6336C"}),
        html.P("Use the radio buttons to filter sales by region.", style={"fontSize": "18px"}),

        # Radio buttons for region filter
        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
            ],
            value="all",
            inline=True,
            style={"margin": "20px", "fontSize": "16px"}
        ),

        # Line chart
        dcc.Graph(id="sales-line-chart")
    ]
)

# Callback to update the chart based on selected region
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):
    if selected_region != "all":
        filtered_df = df[df["region"].str.lower() == selected_region.lower()]
    else:
        filtered_df = df.copy()

    filtered_df = filtered_df.sort_values("date")
    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        color="region",
        title="Pink Morsel Sales Over Time",
        labels={"date": "Date", "sales": "Sales ($)"}
    )

    fig.update_layout(
        title={"x": 0.5, "xanchor": "center"},
        plot_bgcolor="#F9F9F9",
        paper_bgcolor="#F9F9F9",
        font={"size": 14}
    )

    return fig

# Run the app
if __name__ == "__main__":
    app.run(debug=True)