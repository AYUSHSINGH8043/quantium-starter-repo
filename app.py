import pandas as pd
import dash
from dash import html, dcc
import plotly.express as px

# Load processed data
df = pd.read_csv("processed_sales_data.csv")

# Ensure Date column is datetime and sort
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# Create line chart
fig = px.line(
    df,
    x="Date",
    y="Sales",
    color="Region",
    title="Pink Morsel Sales Over Time",
    labels={
        "Date": "Date",
        "Sales": "Total Sales"
    }
)

# Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Impact of Pink Morsel Price Increase on Sales"),
    html.P(
        "This chart shows Pink Morsel sales before and after the price increase on 15 January 2021."
    ),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)
