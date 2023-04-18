import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

from dash import html, dcc, dash_table
from dash.dependencies import Input, Output

from .total_cases_app import app
from .total_cases_chart import chart_layout
from .total_cases_map import map_layout

colors = {
    'background': '#000000',
    'text': '#FFFFFF'
}

app_tabs = html.Div([
        dbc.Tabs(
        [
            dbc.Tab(label="Chart", tab_id='tab-chart', labelClassName="font-weight-bold", activeLabelClassName="text-success"),
            dbc.Tab(label="Map", tab_id='tab-map', labelClassName="font-weight-bold", activeLabelClassName="text-success"),
        ], id='tab-parent', active_tab='tab-chart'
    )
])

app.layout = html.Div(className='w-75 mb-3', children=
    [
        dbc.Card(
            dbc.CardBody(
                [
                    html.H1('Total Confirmed Cases', style={'textAlign': 'left'}),
                    app_tabs,
                    html.Div(id='tab-content', children=[]),
                ]
            ),
        )
    ],
    style={'margin': 'auto', 'width': '100%', 'align-items': 'center'}
)

@app.callback(
    Output(component_id='tab-content', component_property='children'),
    [Input(component_id='tab-parent', component_property='active_tab')]
)

def switch_tab(tab_chosen):
    if tab_chosen == "tab-chart":
        return chart_layout
    
    elif tab_chosen == "tab-map":
        return map_layout
    
    return html.P("This shouldn't be displayed for now...")
