import plotly.express as px
import pandas as pd

from dash import html, dcc
from dash.dependencies import Input, Output

from .weekly_icu_admissions_app import app, weekly_icu_admissions


country_options = [{'label': i, 'value': i,} for i in weekly_icu_admissions['location'].unique()]

chart_layout = html.Div([
    dcc.Graph(id='fig-chart', figure={}),
    
    dcc.Dropdown(id='country-dropdown',
                options=country_options,
                multi=True,
                value=['Bangladesh', 'India', 'China', 'United States'],
                placeholder='Select Country'),
])

@app.callback(
    Output(component_id='fig-chart', component_property='figure'),
    Input(component_id='country-dropdown', component_property='value')
)

def update_chart(country_list):
    dff = weekly_icu_admissions[weekly_icu_admissions['location'].isin(country_list)]
    fig_chart = px.line(
                data_frame=dff, 
                x='date', 
                y='weekly_icu_admissions', 
                color='location',
                labels={'weekly_icu_admissions': '', 'date': ''}, 
                hover_name='location',
                hover_data={'location':False, 'date':True, 'weekly_icu_admissions':True},
                template='plotly_white'
            )
    
    return fig_chart