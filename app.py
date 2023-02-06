#! /usr/bin/env python3
# vim:fenc=utf-8
#
# Copyright © 2023 MiguelHeCa <josemiguel@heca.tech>
#
# Distributed under terms of the MIT license.

"""
Dash app for Income Inequality data
"""
import pandas as pd
import plotly.express as px

from dash import Dash, dcc, html, Input, Output

app = Dash(__name__)

df = pd.read_pickle('data/sptinc_all.pickle')

app.layout = html.Div([
    html.H4("Analysis of the restaurant's revenue"),
    html.P("x-axis:"),
    dcc.Checklist(
        id='x-axis',
        options=['smoker', 'day', 'time', 'sex'],
        value=['time'],
        inline=True
    ),
    html.P("y-axis:"),
    dcc.RadioItems(
        id='y-axis',
        options=['total_bill', 'tip', 'size'],
        value='total_bill',
        inline=True
    ),
    dcc.Graph(id="graph"),
])


@app.callback(
    Output("graph", "figure"),
    Input("x-axis", "value"),
    Input("y-axis", "value"))
def generate_chart(x, y):
    df = px.data.tips() # replace with your own data source
    fig = px.box(df, x=x, y=y)
    return fig


app.run_server(debug=True)
