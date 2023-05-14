import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

from dash import html, dcc, dash_table
from dash.dependencies import Input, Output

from  .layout_app import app
from .cases import cases_layout
from .deaths import death_layout
from .vaccines import vaccine_layout

import dash_bootstrap_components as dbc

import pandas as pd

colors = {
    'background': '#000000',
    'text': '#FFFFFF'
}

app_tabs = html.Div([
        dbc.Tabs(
        [
            dbc.Tab(label="Cases", tab_id='tab-cases', labelClassName="font-weight-bold", activeLabelClassName="text-success"),
            dbc.Tab(label="Deaths", tab_id='tab-deaths', labelClassName="font-weight-bold", activeLabelClassName="text-success"),
            dbc.Tab(label="Vaccinations", tab_id='tab-vaccines', labelClassName="font-weight-bold", activeLabelClassName="text-success"),
        ], id='tab-parent', active_tab='tab-cases'
    )
])

app.layout = html.Div(className='w-75 mb-3 border-warning', children=
    [
        dbc.Card(
            dbc.CardBody(
                [
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
    if tab_chosen == "tab-cases":
        return cases_layout
    
    elif tab_chosen == "tab-deaths":
        return death_layout
    
    elif tab_chosen == "tab-vaccines":
        return vaccine_layout
    
    else:
        return html.P("Select a Tab")
