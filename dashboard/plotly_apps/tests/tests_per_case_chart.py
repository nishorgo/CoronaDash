import plotly.express as px
import pandas as pd

from dash import html, dcc
from dash.dependencies import Input, Output

from .tests_per_case_app import app, tests_per_case

country_list = pd.read_csv('country_list.csv')
country_options = [{'label': i, 'value': i,} for i in country_list['Country']]

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
    dff = tests_per_case[tests_per_case['location'].isin(country_list)]
    fig_chart = px.line(
                data_frame=dff, 
                x='date', 
                y='tests_per_case', 
                color='location',
                labels={'tests_per_case': '', 'date': ''}, 
                hover_name='location',
                hover_data={'location':False, 'date':True, 'tests_per_case':True},
                template='plotly_white'
            )
    
    return fig_chart