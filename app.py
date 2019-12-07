# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_daq as daq
from dash.dependencies import Input, Output
import pandas as pd
import os

pd.set_option('max_columns', None)
data = pd.read_csv('assets/data/tabla_final_google_2.csv')

app = dash.Dash(__name__, external_stylesheets=[
    dbc.themes.BOOTSTRAP,
])

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
    # 'margin': '4px',
}

tab_selected_style = {
    'border': '0px',
    'backgroundColor': '#1D2024',
    'borderBottom': '3px solid #7FFFD4',
    'color': 'white',
    'padding': '6px',
    'fontWeight': 'bold',
    # 'margin': '4px',
}

table_header = [
    html.Thead(html.Tr([html.Th("Feature name"),
                        html.Th("Sensitivity")]))
]

row1 = html.Tr([
    html.Td("Price"),
    html.Td(dcc.Slider(
        id='price_slider',
        min=0,
        max=9,
        value=5,
        step=0.01,
        marks={'0': '0', '9': '9', '5': 'Current'},
        tooltip={'always_visible': True},
        ), className='slider-td'
    )
], className='slider-row')

row2 = html.Tr([
    html.Td("Size (KB)"),
    html.Td(dcc.Slider(
        id='size_slider',
        min=0,
        max=9,
        value=5,
        marks={'0': '0', '9': '9', '5': 'Current'},
        tooltip={'always_visible': True},
        ), className='slider-td'
    )
], className='slider-row')

row3 = html.Tr([
    html.Td("Content Rating"),
    html.Td(dcc.Dropdown(
        id='content_rating_dropdown',
        options=[
            {'label': 'Everyone', 'value': 'Everyone'},
            {'label': 'Teen', 'value': 'Teen'},
            {'label': 'Everyone 10+', 'value': 'Everyone 10+'},
            {'label': 'Adults only 18+', 'value': 'Adults only 18+'},
            {'label': 'Unrated', 'value': 'Unrated'}
        ],
        value=data[data['name'] == 'Airbnb']['Category'].to_list()[0]
,
    )
    )
])

row4 = html.Tr([
    html.Td("Name length"),
    html.Td(dcc.Slider(
        id='length_slider',
        min=0,
        max=9,
        value=5,
        marks={'0': '0', '9': '9', '5': 'Current'},
        tooltip={'always_visible': True},
        ), className='slider-td'
    )
], className='slider-row')

row5 = html.Tr([
    html.Td("Category"),
    html.Td(dcc.Dropdown(
        id='category_dropdown',
        options=[
                {'label': 'EDUCATION', 'value': 'EDUCATION'},
                {'label': 'GAME', 'value': 'GAME'},
                {'label': 'TOOLS', 'value': 'TOOLS'},
                {'label': 'BOOKS_AND_REFERENCE', 'value': 'BOOKS_AND_REFERENCE'},
                {'label': 'ENTERTAINMENT', 'value': 'ENTERTAINMENT'},
                {'label': 'MUSIC_AND_AUDIO', 'value': 'MUSIC_AND_AUDIO'},
                {'label': 'LIFESTYLE', 'value': 'LIFESTYLE'},
                {'label': 'Other', 'value': 'Other'},
                {'label': 'PERSONALIZATION', 'value': 'PERSONALIZATION'},
                {'label': 'FINANCE', 'value': 'FINANCE'},
                {'label': 'BUSINESS', 'value': 'BUSINESS'},
                {'label': 'PRODUCTIVITY', 'value': 'PRODUCTIVITY'},
                {'label': 'NEWS_AND_MAGAZINES', 'value': 'NEWS_AND_MAGAZINES'},
                {'label': 'HEALTH_AND_FITNESS', 'value': 'HEALTH_AND_FITNESS'},
                {'label': 'PHOTOGRAPHY', 'value': 'PHOTOGRAPHY'},
                {'label': 'TRAVEL_AND_LOCAL', 'value': 'TRAVEL_AND_LOCAL'},
                {'label': 'SPORTS', 'value': 'SPORTS'},
                {'label': 'COMMUNICATION', 'value': 'COMMUNICATION'},
                {'label': 'SHOPPING', 'value': 'SHOPPING'},
                {'label': 'SOCIAL', 'value': 'SOCIAL'},
                {'label': 'MAPS_AND_NAVIGATION', 'value': 'MAPS_AND_NAVIGATION'},
                {'label': 'MEDICAL', 'value': 'MEDICAL'},
                {'label': 'FOOD_AND_DRINK', 'value': 'FOOD_AND_DRINK'}
            ],
        )
    )
])

table_body = [html.Tbody([row1, row2, row4, row3, row5])]

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
                            ], color="dark", inverse=True),



                        ], width=3),

                        dbc.Col([
                            dbc.Card([
                                dbc.CardHeader('Features'),
                                dbc.CardBody(
                                    table
                                )

                            ], color="dark", inverse=True)
                        ], width=6),
                        dbc.Col([
                                dbc.Card(
                                    daq.LEDDisplay(
                                      id='my-daq-leddisplay',
                                      value=round(data[data['App Name'] == 'Airbnb']['ind_total_norm'].to_list()[0], 1),
                                    )
                                ),
                                dbc.Card(
                                    dbc.CardBody(
                                        daq.Gauge(
                                            id='score_gauge',
                                            style={
                                                'color': '#1D2024',
                                                'marginBottom': '0px',
                                                'margin-bottom': '0px'
                                            },
                                            min=0.0,
                                            max=5.0,
                                            value=round(data[data['App Name'] == 'Airbnb']['ind_total_norm'].to_list()[0], 2),
                                            size=200,
                                            showCurrentValue=True,
                                            units='Units',
                                            labelPosition='bottom',
                                            label={
                                                'label': 'Success Index',
                                                'style': {
                                                    'color': '#FFFFFF',
                                                    'fontSize': 24
                                                }
                                            }
                                        )
                                    ), color="dark", inverse=True
                                )
                            ]
                            , width=3
                        )

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


@app.callback(
    [Output("price_slider", "value"),
     Output("price_slider", "min"),
     Output("price_slider", "max"),
     Output("price_slider", "marks")
     ],
    [Input("app-name", "value")],
)
def update_price(value):
    v_current = data[data['name'] == value]['Price_1'].to_list()[0]
    v_min = data['Price_1'].min()
    v_max = data['Price_1'].max()
    v_dict = {str(v_min): str(v_min), str(v_max): str(v_max), str(v_current): 'Current'}
    return v_current, v_min, v_max, v_dict


@app.callback(
    [Output("size_slider", "value"),
     Output("size_slider", "min"),
     Output("size_slider", "max"),
     Output("size_slider", "marks")
     ],
    [Input("app-name", "value")],
)
def update_size(value):
    v_current = data[data['name'] == value]['Size'].to_list()[0]
    v_min = data['Size'].min()
    v_max = data['Size'].max()
    v_dict = {str(v_min): str(v_min), str(v_max): str(v_max), str(v_current): 'Current'}
    return v_current, v_min, v_max, v_dict


@app.callback(
    [Output("length_slider", "value"),
     Output("length_slider", "min"),
     Output("length_slider", "max"),
     Output("length_slider", "marks")
     ],
    [Input("app-name", "value")],
)
def update_length(value):
    v_current = data[data['name'] == value]['tamano_nombre'].to_list()[0]
    v_min = data['tamano_nombre'].min()
    v_max = data['tamano_nombre'].max()
    v_dict = {str(v_min): str(v_min), str(v_max): str(v_max), str(v_current): 'Current'}
    return v_current, v_min, v_max, v_dict


@app.callback(
    Output("content_rating_dropdown", "value"),
    [Input("app-name", "value")],
)
def update_content_rating_dropdown(value):
    v_current = data[data['name'] == value]['Content Rating'].to_list()[0]
    return v_current


@app.callback(
    Output("category_dropdown", "value"),
    [Input("app-name", "value")],
)
def update_category_dropdown(value):
    v_current = data[data['name'] == value]['Category'].to_list()[0]
    return v_current


@app.callback(
    Output("score_gauge", "value"),
    [Input("app-name", "value")],
)
def update_score_gauge(value):
    v_current = round(data[data['App Name'] == value]['ind_total_norm'].to_list()[0], 2)
    return v_current


@app.callback(
    Output("my-daq-leddisplay", "value"),
    [Input("app-name", "value")],
)
def update_score_leddisplay(value):
    v_current = round(data[data['App Name'] == value]['ind_total_norm'].to_list()[0], 1)
    return v_current





if __name__ == '__main__':
    app.run_server(debug=True)