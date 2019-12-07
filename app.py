# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pandas as pd
import os

pd.set_option('max_columns', None)
data = pd.read_csv('assets/data/tabla_final_google_1.csv')

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

GOBIERNO_LOGO = "assets/images/col-gov-logo.8504ab3d.png"
DS4A_LOGO = "assets/images/DS4A Colombia.png"

tabs_styles = {
    'height': '44px'
}

tab_style = {
    'border': '0px',
    'backgroundColor': '#1D2024',
    'borderBottom': '3px solid #1D2024',
    'padding': '6px',
    'color': 'white',
    'margin': '4px',
}

tab_selected_style = {
    'border': '0px',
    'backgroundColor': '#1D2024',
    'borderBottom': '3px solid #7FFFD4',
    'color': 'white',
    'padding': '6px',
    'fontWeight': 'bold',
    'margin': '4px',
}

table_header = [
    html.Thead(html.Tr([html.Th("Feature name"),
                        html.Th("Sensitivity")]))
]

row1 = html.Tr([
    html.Td("Price"),
    html.Td(dcc.Slider(
        min=0,
        max=9,
        value=5,
        marks={'0': '0', '9': '9', '5': 'Current'},
        tooltip={'always_visible': True},
        )
    )
])

row2 = html.Tr([
    html.Td("Size (KB)"),
    html.Td(dcc.Slider(
        min=0,
        max=9,
        value=5,
        marks={'0': '0', '9': '9', '5': 'Current'},
        tooltip={'always_visible': True},
        )
    )
])

row3 = html.Tr([
    html.Td("Content Rating"),
    html.Td(dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL',
    )
    )
])

row4 = html.Tr([
    html.Td("Name length"),
    html.Td(dcc.Slider(
        min=0,
        max=9,
        value=5,
        marks={'0': '0', '9': '9', '5': 'Current'},
        tooltip={'always_visible': True},
    )
    )

])

row5 = html.Tr([
    html.Td("Category"),
    html.Td(dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL',
    )
    )
])

table_body = [html.Tbody([row1, row2, row3, row4, row5])]

table = dbc.Table(
    # using the same table as in the above example
    table_header + table_body,
    bordered=True,
    dark=True,
    hover=True,
    responsive=True,
    striped=True,
)

app.layout = html.Div([


    dbc.Navbar(
        [
            dbc.Col([
                html.Div(dbc.NavbarBrand("GOOGLE PLAY DASHBOARD", className="ml-2")),
                html.Div(dbc.NavbarBrand(html.Small("Successing App Analysis for Investors and Developers", className="ml-2"))),
            ]),
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=DS4A_LOGO, height="30px")),
                        dbc.Col(html.Img(src=GOBIERNO_LOGO, height="30px")),
                    ],
                    align="center",
                    no_gutters=True,
                ),
                href="https://plot.ly",
            )
        ],
        color="dark",
        dark=True,
    ),

    html.Div(className='container-fluid', children=[
        dcc.Tabs([
                dcc.Tab(label='FOR INVESTORS', children=[

                ], style=tab_style, selected_style=tab_selected_style),
                dcc.Tab(label='FOR DEVELOPERS', children=[
                    dbc.Row([
                        dbc.Col([

                            dbc.Card([
                                dbc.CardBody(
                                    dbc.FormGroup([
                                        dbc.Label("App Name", html_for="example-email"),
                                        dbc.Input(type="text", id="app-name", placeholder="App name", value='Airbnb'),
                                        dbc.Label("App Image", html_for="example-email"),
                                        html.Div(
                                            # html.Img(id='app-img', src='https://via.placeholder.com/180'),
                                            html.Img(id='app-img', src='assets/images/apps-imgs/Airbnb.png'),
                                        )
                                    ], style={'margin-left': '4px'})
                                )
                            ]),



                        ], width=3),

                        dbc.Col([
                            dbc.Card([
                                dbc.CardHeader('Features'),
                                dbc.CardBody(
                                    table
                                )

                            ])
                        ], width=6),
                        dbc.Col(
                         width=3),
                    ])
                ], style=tab_style, selected_style=tab_selected_style),
            ],
        )

    ], style={'background-color': '#343a40'}),

])


@app.callback(
    Output("app-img", "src"),
    [Input("app-name", "value")],
)
def update_output(value):
    if os.path.isfile('assets/images/apps-imgs/' + value + '.png'):
        return 'assets/images/apps-imgs/' + value + '.png'
    else:
        return 'https://via.placeholder.com/180'


if __name__ == '__main__':
    app.run_server(debug=True)