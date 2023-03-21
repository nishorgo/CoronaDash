import pandas as pd
import plotly.express as px

from dash import html, dcc
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash

app = DjangoDash('DailyCases')

colors = {
    'background': '#000000',
    'text': '#FFFFFF'
}

# Import and clean data (importing csv into pandas)
df = pd.read_csv('owid-covid-data.csv')
daily_case = df[['date', 'location', 'new_cases', 'new_cases_smoothed']].copy()

app.layout = html.Div([

    dcc.Dropdown(id='country_dropdown',
                    options=[{'label': i, 'value': i,} for i in daily_case['location'].unique()],
                    multi=True,
                    value=['Bangladesh', 'India', 'China', 'United States'],
                    style={'width': "50%"}),

    dcc.Graph(id='daily_cases', figure={})
])

@app.callback(
    [Output(component_id='daily_cases', component_property='figure')],
    [Input(component_id='country_dropdown', component_property='value')]
)

def update_graph(country_list):
    dff = daily_case[daily_case['location'].isin(country_list)]
    fig = px.line(dff, x='date', y='new_cases_smoothed', color='location', title='Daily Cases', template='plotly_white')
    return [fig]

