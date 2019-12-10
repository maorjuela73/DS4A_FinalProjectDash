# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_daq as daq
from dash.dependencies import Input, Output
import pandas as pd
import os
import pickle

pd.set_option('max_columns', None)
data = pd.read_csv('assets/data/tabla_final_google_2.csv')

with open('assets/model/logit.pkl', 'rb') as f:
    logit_res = pickle.load(f)

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
    'borderBottom': '5px solid #1D2024',
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

app.layout = html.Div([

    dbc.Navbar(
        [
            dbc.Col([
                html.Div(dbc.NavbarBrand("GOOGLE PLAY DASHBOARD", className="ml-2")),
                html.Div(dbc.NavbarBrand(
                    html.Small("Successing App Analysis for Investors and Developers", className="ml-2"))),
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
                            dbc.CardBody([
                                html.H4('Application Search'),
                                dbc.Form([
                                    dbc.FormGroup([
                                        dbc.Label("App Name", html_for="example-email"),
                                        dbc.Input(type="text", id="app-name", placeholder="App name", value='Airbnb'),
                                    ]),
                                    dbc.Button('Search', id='search-app-btn', color="primary", block=True),
                                ], style={})
                            ])
                        ], color="dark", inverse=True),
                        dbc.Card([
                            dbc.CardBody([
                                html.H4('Logo', className='imagelogo-title'),
                                html.Div(
                                    # html.Img(id='app-img', src='https://via.placeholder.com/180'),
                                    html.Img(id='app-img', src='assets/images/apps-imgs/Airbnb.png',
                                             className='img-fluid rounded mx-auto d-block'),
                                ),
                            ])
                        ], color="dark", inverse=True),

                    ], width=3),

                    dbc.Col([
                        dbc.Card([
                            # dbc.CardHeader('Features'),
                            dbc.CardBody([
                                html.H4('Features'),
                                dbc.Row([
                                    dbc.Col(html.H6(['Price ']), width=4),
                                    dbc.Col(dcc.Slider(
                                        id='price_slider',
                                        min=0,
                                        max=9,
                                        value=5,
                                        step=0.01,
                                        marks={'0': '0', '9': '9', '5': 'Current'},
                                        tooltip={'always_visible': False},
                                    ), className='slider-td'
                                    ),
                                ]),
                                dbc.Row([
                                    dbc.Col(html.H6(['Size (KB) ']), width=4),
                                    dbc.Col(dcc.Slider(
                                        id='size_slider',
                                        min=0,
                                        max=9,
                                        value=5,
                                        marks={'0': '0', '9': '9', '5': 'Current'},
                                        tooltip={'always_visible': False},
                                    ), className='slider-td'
                                    ),
                                ]),
                                dbc.Row([
                                    dbc.Col(html.H6(['Name length ']), width=4),
                                    dbc.Col(dcc.Slider(
                                        id='length_slider',
                                        min=0,
                                        max=9,
                                        value=5,
                                        marks={'0': '0', '9': '9', '5': 'Current'},
                                        tooltip={'always_visible': False},
                                    ), className='slider-td'
                                    ),
                                ]),
                                dbc.Row([
                                    dbc.Col(html.H6(['Category ']), width=4),
                                    dbc.Col(dcc.Dropdown(
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
                                    ),
                                ]),
                                dbc.Row([
                                    dbc.Col(html.H6(['Content Rating ']), width=4),
                                    dbc.Col(dcc.Dropdown(
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
                                    ),
                                ]),
                            ]
                            )

                        ], color="dark", inverse=True, className='features-card')
                    ], width=6),
                    dbc.Col([
                        dbc.Card(
                            dbc.CardBody([
                                html.H4('Current Score'),
                                html.Div(
                                    daq.LEDDisplay(
                                        id='my-daq-leddisplay',
                                        value=round(data[data['App Name'] == 'Airbnb']['ind_total_norm'].to_list()[0], 1),
                                        backgroundColor="#1D2024",
                                        style={"textAlign": "center", "width": "0%"},
                                    )
                                ),
                            ]), color="dark", inverse=True
                        ),
                        dbc.Card(
                            dbc.CardBody([
                                html.H4('Simulated Score'),
                                html.Div(
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
                                        # labelPosition='bottom',
                                        # label={
                                        #     'label': 'Success Index',
                                        #     'style': {
                                        #         'color': '#FFFFFF',
                                        #         'fontSize': 24
                                        #     }
                                        # }
                                    )
                                ),

                            ]), color="dark", inverse=True
                        )], width=3
                    )

                ], className='')
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


# @app.callback(
#     Output("score_gauge", "value"),
#     [Input("app-name", "value")],
# )
# def update_score_gauge(value):
#     v_current = round(data[data['App Name'] == value]['ind_total_norm'].to_list()[0], 2)
#     return v_current


@app.callback(
    Output("my-daq-leddisplay", "value"),
    [Input("app-name", "value")],
)
def update_score_leddisplay(value):
    v_current = round(data[data['App Name'] == value]['ind_total_norm'].to_list()[0], 1)
    return v_current


@app.callback(
    Output("score_gauge", "value"),
    [Input("app-name", "value"),
     Input("price_slider", "value"),
     Input("size_slider", "value"),
     Input("length_slider", "value"),
     Input("content_rating_dropdown", "value"),
     Input("category_dropdown", "value")]
)
def puntuar(name_p,price_p,size_p,name_length_p,content_p,category_p):
    df = data
    aux=pd.DataFrame()
    aux=df[df['name']==name_p][['Intercept','Price_1','Size','Latest_Version','days_since_last_up','tamano_nombre','Category_BOOKS_AND_REFERENCE','Category_BUSINESS','Category_COMMUNICATION','Category_EDUCATION','Category_ENTERTAINMENT','Category_FINANCE','Category_FOOD_AND_DRINK','Category_GAME','Category_HEALTH_AND_FITNESS','Category_LIFESTYLE','Category_MAPS_AND_NAVIGATION','Category_MEDICAL','Category_MUSIC_AND_AUDIO','Category_NEWS_AND_MAGAZINES','Category_Other','Category_PERSONALIZATION','Category_PHOTOGRAPHY','Category_PRODUCTIVITY','Category_SHOPPING','Category_SOCIAL','Category_SPORTS','Category_TOOLS','Content_Rating_Everyone_10','Content_Rating_Adults_only_18','Content_Rating_Teen','Content_Rating_Unrated','Minimum_Version_depends_on_device_0']]
    aux['Price_1']=price_p
    aux['Size']=size_p
    aux['tamano_nombre']=name_length_p
    ###content_rating
    content_aux=''
    if content_p=='Everyone 10+':
            content_aux='Content_Rating_Everyone_10'
    if content_p=='Teen':
            content_aux='Content_Rating_Teen'
    if content_p=='Adults only 18+':
            content_aux='Content_Rating_Adults_only_18'
    if content_p=='Unrated':
            content_aux='Content_Rating_Unrated'
    for i in ['Content_Rating_Everyone_10','Content_Rating_Adults_only_18','Content_Rating_Teen','Content_Rating_Unrated']:
        if i==content_aux:
                aux[i]=1
        else:
                aux[i]=0
    ###category
    category_aux='Category_'+category_p
    for i in ['Category_BOOKS_AND_REFERENCE','Category_BUSINESS','Category_COMMUNICATION','Category_EDUCATION','Category_ENTERTAINMENT','Category_FINANCE','Category_FOOD_AND_DRINK','Category_GAME','Category_HEALTH_AND_FITNESS','Category_LIFESTYLE','Category_MAPS_AND_NAVIGATION','Category_MEDICAL','Category_MUSIC_AND_AUDIO','Category_NEWS_AND_MAGAZINES','Category_Other','Category_PERSONALIZATION','Category_PHOTOGRAPHY','Category_PRODUCTIVITY','Category_SHOPPING','Category_SOCIAL','Category_SPORTS','Category_TOOLS']:
        if i==category_aux:
                aux[i]=1
        else:
                aux[i]=0

    # testreturn = df[df['name'] == name_p][['Intercept', 'Price_1', 'Size', 'Latest_Version', 'days_since_last_up', 'tamano_nombre',
    #                           'Category_BOOKS_AND_REFERENCE', 'Category_BUSINESS', 'Category_COMMUNICATION',
    #                           'Category_EDUCATION', 'Category_ENTERTAINMENT', 'Category_FINANCE',
    #                           'Category_FOOD_AND_DRINK', 'Category_GAME', 'Category_HEALTH_AND_FITNESS',
    #                           'Category_LIFESTYLE', 'Category_MAPS_AND_NAVIGATION', 'Category_MEDICAL',
    #                           'Category_MUSIC_AND_AUDIO', 'Category_NEWS_AND_MAGAZINES', 'Category_Other',
    #                           'Category_PERSONALIZATION', 'Category_PHOTOGRAPHY', 'Category_PRODUCTIVITY',
    #                           'Category_SHOPPING', 'Category_SOCIAL', 'Category_SPORTS', 'Category_TOOLS',
    #                           'Content_Rating_Everyone_10', 'Content_Rating_Adults_only_18', 'Content_Rating_Teen',
    #                           'Content_Rating_Unrated', 'Minimum_Version_depends_on_device_0']]

    score_actual=(logit_res.predict(df[df['name']==name_p][['Intercept','Price_1','Size','Latest_Version','days_since_last_up','tamano_nombre','Category_BOOKS_AND_REFERENCE','Category_BUSINESS','Category_COMMUNICATION','Category_EDUCATION','Category_ENTERTAINMENT','Category_FINANCE','Category_FOOD_AND_DRINK','Category_GAME','Category_HEALTH_AND_FITNESS','Category_LIFESTYLE','Category_MAPS_AND_NAVIGATION','Category_MEDICAL','Category_MUSIC_AND_AUDIO','Category_NEWS_AND_MAGAZINES','Category_Other','Category_PERSONALIZATION','Category_PHOTOGRAPHY','Category_PRODUCTIVITY','Category_SHOPPING','Category_SOCIAL','Category_SPORTS','Category_TOOLS','Content_Rating_Everyone_10','Content_Rating_Adults_only_18','Content_Rating_Teen','Content_Rating_Unrated','Minimum_Version_depends_on_device_0']])).to_list()[0]
    puntuacion_actual=df[df['name']==name_p]['ind_total_norm'].to_list()[0]
    nuevo_score=logit_res.predict(aux).to_list()[0]
    nueva_puntuacion=((nuevo_score*puntuacion_actual)/score_actual)
    if nueva_puntuacion>=5 :
        nueva_puntuacion=5
    if nueva_puntuacion<0 :
        nueva_puntuacion=0
    return nueva_puntuacion


if __name__ == '__main__':
    app.run_server(debug=True)
