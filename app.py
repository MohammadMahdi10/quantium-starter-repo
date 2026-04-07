# app.py
import pandas as pd
from dash import Dash, dcc, html

df = pd.read_csv("formatted_output.csv")

df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser"),
    
    dcc.Graph(
        id="sales-line-chart",
        figure={
            "data": [
                {"x": df["date"], "y": df["sales"], "type": "line", "name": "Sales"}
            ],
            "layout": {
                "title": "Daily Pink Morsel Sales",
                "xaxis": {"title": "Date"},
                "yaxis": {"title": "Sales ($)"},
            }
        }
    )
])

if __name__ == "__main__":
    app.run(debug=True)