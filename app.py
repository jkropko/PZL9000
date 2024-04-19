import numpy as np
import pandas as pd
import requests
import json
import plotly.express as px
import plotly.figure_factory as ff
import dash
from datetime import timedelta
from dash import dcc
from dash import html
from dash import dash_table
from dash.dependencies import Input, Output, State
import pzl

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'PZL9000'

app.layout = html.Div(
    [
        html.H1("The Puzzle Hunt Solutions Desk", style={'font-size': '60px'}),

        dcc.Markdown("Lost? Confused? Unsure? Ask me, PZL9000, the world’s first AI Puzzle Bot. I am, by any practical definition of the word, foolproof and incapable of error. Except that I seem to have come down with a computer virus. Achoo!"),

        html.Img(src=app.get_asset_url('pzl9000.png'), style = {'width':'20%', 'textAlign': 'center'}),

         dcc.Store(id='friend', storage_type='local', clear_data=True),

         dcc.Store(id='n', storage_type='session', clear_data=True),

         dcc.Textarea(id="input",
                       value="Type your question for PZL9000 here",
                       style={'width': '100%', 'height': 100}),

         html.Button('Submit', id='button', n_clicks=0, style={'fontSize': '36px'}),

#         html.Div(id='load'),

         html.Div(id='output')
    ], style = {'textAlign': 'center', 'font-size': '48px'}
    )

#@app.callback(Output('load', 'children'),
#              [Input('button', 'n_clicks')])

#def prepare_data(n_clicks):
#    if n_clicks>0:
#        return html.Div([dcc.Markdown('')], id='output')

@app.callback(
    [Output('output', 'children'),
     Output('n', 'data'),
     Output('friend', 'data')],
    [Input('button', 'n_clicks')],
    [State('input', 'value'),
     State('n', 'data'),
     State('friend', 'data')]
)

def update_output(n_clicks, value, n, friend):
    if value=='Type your question for PZL9000 here':
        response = 'What do you want?'
        new_n = 0
        new_friend = False
        result = (response, new_n, new_friend)
    elif value=='':
        response = ''
        new_n = 0
        new_friend = False
        result = (response, new_n, new_friend)
    elif value.lower().strip() in ['gesundheit', 'bless you', 'god bless you']:
        response = 'Thanks. I mean, you can still talk to me. Just be polite and say gesundheit or bless you before asking your question. Achoo!'
        new_n = 0
        new_friend = False
        result = (response, new_n, new_friend)
    else:
        result = pzl.pzl(value, n, friend)
        response = result[0]
        new_n = result[1]
        new_friend = result[2]
    return [response, new_n, new_friend]

if __name__ == '__main__':
    app.run_server(debug=False, use_reloader=False, port=8050)