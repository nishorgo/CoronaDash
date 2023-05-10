import plotly.express as px
import pandas as pd

from dash import html, dcc
from dash.dependencies import Input, Output

from .daily_cases_app import app, daily_case


# selecting only the country names
country_options = [{'label': i, 'value': i,} for i in daily_case['location'].unique()]

# main chart layout
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
    dff = daily_case[daily_case['location'].isin(country_list)]
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