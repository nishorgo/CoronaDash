import plotly.express as px
import pandas as pd

from dash import html, dcc
from dash.dependencies import Input, Output

from .daily_people_vaccinated_app import app, daily_people_vaccinated


country_options = [{'label': i, 'value': i,} for i in daily_people_vaccinated['location'].unique()]

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
    dff = daily_people_vaccinated[daily_people_vaccinated['location'].isin(country_list)]
    fig_chart = px.line(
                data_frame=dff, 
                x='date', 
                y='new_people_vaccinated_smoothed', 
                color='location',
                labels={'new_people_vaccinated_smoothed': '', 'date': ''}, 
                hover_name='location',
                hover_data={'location':False, 'date':True, 'new_people_vaccinated_smoothed':True},
                template='plotly_white'
            )
    
    return fig_chart