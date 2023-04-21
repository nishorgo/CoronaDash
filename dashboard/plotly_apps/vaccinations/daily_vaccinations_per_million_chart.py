import plotly.express as px
import pandas as pd

from dash import html, dcc
from dash.dependencies import Input, Output

from .daily_vaccinations_per_million_app import app, daily_vaccinations_per_million

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
    dff = daily_vaccinations_per_million[daily_vaccinations_per_million['location'].isin(country_list)]
    fig_chart = px.line(
                data_frame=dff, 
                x='date', 
                y='new_vaccinations_smoothed_per_million', 
                color='location',
                labels={'new_vaccinations_smoothed_per_million': '', 'date': ''}, 
                hover_name='location',
                hover_data={'location':False, 'date':True, 'new_vaccinations_smoothed_per_million':True},
                template='plotly_white'
            )
    
    return fig_chart