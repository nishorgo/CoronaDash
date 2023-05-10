import plotly.express as px
import pandas as pd

from dash import html, dcc
from dash.dependencies import Input, Output

from .positive_rate_app import app, positive_rate


country_options = [{'label': i, 'value': i,} for i in positive_rate['location'].unique()]

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
    dff = positive_rate[positive_rate['location'].isin(country_list)]
    fig_chart = px.line(
                data_frame=dff, 
                x='date', 
                y='positive_rate', 
                color='location',
                labels={'positive_rate': '', 'date': ''}, 
                hover_name='location',
                hover_data={'location':False, 'date':True, 'positive_rate':True},
                template='plotly_white'
            )
    
    return fig_chart