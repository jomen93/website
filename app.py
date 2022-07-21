from dash import Dash, dcc, html 
from flask import Flask
import dash_bootstrap_components as dbc
import os


dash_app = Dash(__name__, external_stylesheets=[dbc.themes.COSMO])
dash_app.title = "Portafolio"
LOAD = True
#app = dash_app.server


foto = html.Img(
    src = dash_app.get_asset_url("foto.jpeg"), style={"width":"50%", "height":"80%"}
    )

Header = html.Div([
    dbc.Row([
        dbc.Col(html.H1(foto), md=2),
        dbc.Col([
            html.Div([html.H1("Johan S. Méndez")], style={"height":"20%", "textAlign":"center"}),
            html.Div([html.H2("Científico de datos")], style={"height":"20%", "textAlign":"center"}),
            html.Div([html.H3("MsC. Physics UNAM")], style={"height":"20%", "textAlign":"center"}),
            html.Div([html.H4("Bs. Physics UNAL")], style={"height":"20%", "textAlign":"center"}),
            ], md=10),
        ]),
    html.Br(),
    ])


Tabs = html.Div([
    dbc.Row([
        dbc.Col([
            dbc.Tabs([
                dbc.Tab(label="Home", id="home"),
                dbc.Tab(label="Projects"),
                dbc.Tab(label="Exercises"),
                dbc.Tab(label="Hobbies"),
                dbc.Tab(label="Contact"),
                ])
            ])
        ])
    ])


Footer = html.Footer([
    "Hola"
    ])




dash_app.layout = dbc.Container(
    fluid = True,
    children = [
        Header,
        Tabs,
        Footer
        ]
    )  



if __name__ == "__main__":
    dash_app.run_server(
        debug = True,
        host = "0.0.0.0",
        port = os.getenv("PORT", 8000),
        dev_tools_hot_reload=True
            )




