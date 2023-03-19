import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# Import and clean data (importing csv into pandas)
df = pd.read_csv('owid-covid-data.csv')
daily_case = df[['date', 'location', 'new_cases', 'new_cases_smoothed']].copy()

app.layout = html.Div([
    html.H1('Daily Cases', style={'text-align': 'center'}),

    dcc.Dropdown(id='country_drop',
                    options=[{'label': i, 'value': i} for i in daily_case['location'].unique()],
                    multi=True,
                    value=['Bangladesh', 'India', 'China', 'United States'], 
                    style={'width': "40%"}),

    dcc.Graph(id='daily_cases', figure={})
])

@app.callback(
    [Output(component_id='daily_cases', component_property='figure')],
    [Input(component_id='country_drop', component_property='value')]
)

def update_graph(country_list):
    dff = daily_case[daily_case['location'].isin(country_list)]
    fig = px.line(dff, x='date', y='new_cases_smoothed', color='location', title='Daily Cases')
    return [fig]

