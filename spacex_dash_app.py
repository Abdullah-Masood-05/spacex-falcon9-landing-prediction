import os
import pandas as pd
import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Load dataset
spacex_df = pd.read_csv("spacex_launch_dash.csv")
min_payload = spacex_df["Payload Mass (kg)"].min()
max_payload = spacex_df["Payload Mass (kg)"].max()

# Initialize Dash app with Bootstrap theme
app = dash.Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.FLATLY,
        "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css"
    ],
)
app.title = "SpaceX Launch Dashboard"
server = app.server  # For Render deployment

# Navbar
navbar = dbc.NavbarSimple(
    brand="SpaceX Launch Dashboard",
    brand_href="#",
    color="dark",
    dark=True,
    children=[
        dbc.NavItem(
            dbc.NavLink(
                [
                    html.I(className="bi bi-github", style={"font-size": "1.2rem", "margin-right": "5px"}),
                    "GitHub"
                ],
                href="https://github.com/Abdullah-Masood-05",
                target="_blank"
            )
        ),
    ],
)

# Filter controls (dropdown and range slider)
controls = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Filters", className="card-title mb-3"),
            dcc.Dropdown(
                id="site-dropdown",
                options=[
                    {"label": "All Sites", "value": "ALL"},
                    *[
                        {"label": site, "value": site}
                        for site in spacex_df["Launch Site"].unique()
                    ],
                ],
                value="ALL",
                clearable=False,
                style={"width": "100%"},
            ),
            html.Br(),
            html.Label("Payload Range (Kg):"),
            dcc.RangeSlider(
                id="payload-slider",
                min=0,
                max=10000,
                step=500,
                marks={i: str(i) for i in range(0, 10001, 2500)},
                value=[min_payload, max_payload],
                tooltip={"placement": "bottom", "always_visible": False},
            ),
        ]
    ),
    className="shadow-sm",
)

# Pie chart card
pie_card = dbc.Card(
    dbc.CardBody(
        dcc.Graph(id="success-pie-chart", config={"displayModeBar": False})
    ),
    className="shadow-sm",
)

# Scatter plot card
scatter_card = dbc.Card(
    dbc.CardBody(
        dcc.Graph(id="success-payload-scatter-chart", config={"displayModeBar": False})
    ),
    className="shadow-sm",
)

# App Layout
app.layout = dbc.Container(
    [
        navbar,
        html.Br(),
        dbc.Row(
            [
                dbc.Col(controls, xs=12, md=3),
                dbc.Col(pie_card, xs=12, md=9),
            ],
            className="g-3",
        ),
        dbc.Row(
            dbc.Col(scatter_card, xs=12),
            className="g-3",
        ),
    ],
    fluid=True,
)

# Pie chart callback
@app.callback(
    Output("success-pie-chart", "figure"),
    Input("site-dropdown", "value")
)
def update_pie_chart(selected_site):
    if selected_site == "ALL":
        fig = px.pie(
            spacex_df,
            values="class",
            names="Launch Site",
            title="Total Successful Launches by Site",
            color_discrete_sequence=px.colors.qualitative.Set3,
        )
    else:
        df = spacex_df[spacex_df["Launch Site"] == selected_site]
        fig = px.pie(
            df,
            names="class",
            title=f"Success vs Failure at {selected_site}",
            color_discrete_map={1: "#2ECC71", 0: "#E74C3C"},
        )
    fig.update_layout(margin=dict(l=20, r=20, t=40, b=20))
    return fig

# Scatter plot callback
@app.callback(
    Output("success-payload-scatter-chart", "figure"),
    [Input("site-dropdown", "value"), Input("payload-slider", "value")]
)
def update_scatter_plot(selected_site, payload_range):
    low, high = payload_range
    dff = spacex_df[
        (spacex_df["Payload Mass (kg)"] >= low)
        & (spacex_df["Payload Mass (kg)"] <= high)
    ]
    if selected_site != "ALL":
        dff = dff[dff["Launch Site"] == selected_site]

    fig = px.scatter(
        dff,
        x="Payload Mass (kg)",
        y="class",
        color="Booster Version",
        symbol="class",
        title=f"Payload vs Launch Outcome: {'All Sites' if selected_site == 'ALL' else selected_site}",
        color_discrete_sequence=px.colors.qualitative.Set2,
    )
    fig.update_layout(margin=dict(l=20, r=20, t=40, b=20))
    return fig

# Run server
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8050))
    app.run(host="0.0.0.0", port=port)