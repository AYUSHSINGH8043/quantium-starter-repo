import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Load processed data
df = pd.read_csv("processed_sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# Create Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div(
    style={
        "fontFamily": "Arial",
        "backgroundColor": "#f4f6f8",
        "padding": "30px"
    },
    children=[
        html.H1(
            "Pink Morsel Sales Dashboard",
            style={"textAlign": "center", "color": "#333"}
        ),

        html.P(
            "Visualising Pink Morsel sales before and after the price increase (15 Jan 2021)",
            style={"textAlign": "center", "color": "#666"}
        ),

        html.Div(
            style={
                "width": "300px",
                "margin": "20px auto",
                "textAlign": "center"
            },
            children=[
                html.Label("Select Region", style={"fontWeight": "bold"}),
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
                    inline=True
                ),
            ],
        ),

        dcc.Graph(id="sales-line-chart"),
    ],
)

# Callback to update chart
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value"),
)
def update_chart(selected_region):
    if selected_region != "all":
        filtered_df = df[df["Region"] == selected_region]
    else:
        filtered_df = df

    fig = px.line(
        filtered_df,
        x="Date",
        y="Sales",
        color="Region",
        title="Pink Morsel Sales Over Time",
        labels={
            "Date": "Date",
            "Sales": "Total Sales ($)",
            "Region": "Region"
        }
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        title_x=0.5
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)
