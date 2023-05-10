import plotly.express as px
import pandas as pd

from dash import html, dcc
from dash.dependencies import Input, Output

from .icu_patients_app import app, icu_patients


country_options = [{'label': i, 'value': i,} for i in icu_patients['location'].unique()]

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
    dff = icu_patients[icu_patients['location'].isin(country_list)]
    fig_chart = px.line(
                data_frame=dff, 
                x='date', 
                y='icu_patients', 
                color='location',
                labels={'icu_patients': '', 'date': ''}, 
                hover_name='location',
                hover_data={'location':False, 'date':True, 'icu_patients':True},
                template='plotly_white'
            )
    
    return fig_chart