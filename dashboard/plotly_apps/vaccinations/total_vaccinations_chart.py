import plotly.express as px
import pandas as pd

from dash import html, dcc
from dash.dependencies import Input, Output

from .total_vaccinations_app import app, total_vaccinations


country_options = [{'label': i, 'value': i,} for i in total_vaccinations['location'].unique()]

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
    dff = total_vaccinations[total_vaccinations['location'].isin(country_list)]
    fig_chart = px.line(
                data_frame=dff, 
                x='date', 
                y='total_vaccinations', 
                color='location',
                labels={'total_vaccinations': '', 'date': ''}, 
                hover_name='location',
                hover_data={'location':False, 'date':True, 'total_vaccinations':True},
                template='plotly_white'
            )
    
    return fig_chart