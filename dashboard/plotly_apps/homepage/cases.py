from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

from dash import html, dcc
from dash.dependencies import Input, Output
from .layout_app import app, daily_cases

import pandas as pd

country_list = pd.read_csv('country_list.csv')
country_options = [{'label': i, 'value': i,} for i in country_list['Country']]

cases_layout = html.Div([
    dcc.Graph(id='fig-cases', figure={}),
    
    dcc.Dropdown(id='country-dropdown',
                options=country_options,
                multi=True,
                value=['Bangladesh', 'India', 'China', 'United States'],
                placeholder='Select Country'),
])



@app.callback(
    Output(component_id='fig-cases', component_property='figure'),
    Input(component_id='country-dropdown', component_property='value')
)

def update_chart(country_list):
    dff = daily_cases[daily_cases['location'].isin(country_list)]
    fig_chart = px.line(
                data_frame=dff, 
                x='date', 
                y='new_cases_smoothed', 
                color='location',
                labels={'new_cases_smoothed': '', 'date': ''}, 
                hover_name='location',
                hover_data={'location':False, 'date':True, 'new_cases_smoothed':True},
                template='plotly_white'
            )
    
    return fig_chart