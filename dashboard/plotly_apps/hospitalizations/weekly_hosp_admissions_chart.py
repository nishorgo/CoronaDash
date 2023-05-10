import plotly.express as px
import pandas as pd

from dash import html, dcc
from dash.dependencies import Input, Output

from .weekly_hosp_admissions_app import app, weekly_hosp_admissions


country_options = [{'label': i, 'value': i,} for i in weekly_hosp_admissions['location'].unique()]

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
    dff = weekly_hosp_admissions[weekly_hosp_admissions['location'].isin(country_list)]
    fig_chart = px.line(
                data_frame=dff, 
                x='date', 
                y='weekly_hosp_admissions', 
                color='location',
                labels={'weekly_hosp_admissions': '', 'date': ''}, 
                hover_name='location',
                hover_data={'location':False, 'date':True, 'weekly_hosp_admissions':True},
                template='plotly_white'
            )
    
    return fig_chart