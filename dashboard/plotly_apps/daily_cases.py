import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

from dash import html, dcc, dash_table
from dash.dependencies import Input, Output

from .app import app
from .chart import chart_layout

colors = {
    'background': '#000000',
    'text': '#FFFFFF'
}

# Import and clean data (importing csv into pandas)
df = pd.read_csv('owid-covid-data.csv')
daily_case = df[['iso_code', 'continent', 'date', 'location', 'new_cases', 'new_cases_smoothed']].copy()
country_list = ['Bangladesh', 'India', 'China', 'United States']
dff = daily_case[daily_case['location'].isin(country_list)]
country_list = pd.read_csv('country_list.csv')
country_options = [{'label': i, 'value': i,} for i in country_list['Country']]

cc_scale = ['#fee5d9', '#fcbba1', '#fc9272', '#fb6a4a', '#ef3b2c', '#cb181d', '#a50f15', '#67000d', '#4a1486', '#1a0000']



fig_map = px.choropleth(
                    df, 
                    locations="iso_code", 
                    color="new_cases_smoothed", 
                    hover_name="location", 
                    animation_frame="date", 
                    color_continuous_scale=cc_scale,
                    labels={'new_cases_smoothed': 'daily cases'},
                    hover_data=['new_cases_smoothed', 'date'],
                    range_color=(0, 600000),
                    height=600,
                    width=1000,
                    template='plotly_white'
                )

fig_table = dash_table.DataTable(id='my_table', columns=[{'name': col, 'id': col} for col in ['date', 'location', 'new_cases']])

app_tabs = html.Div([
        dbc.Tabs(
        [
            dbc.Tab(label="Chart", tab_id='tab-chart', labelClassName="text-success font-weight-bold", activeLabelClassName="text-danger"),
            dbc.Tab(label="Map", tab_id='tab-map', labelClassName="text-success font-weight-bold", activeLabelClassName="text-danger"),
            #dcc.Tab(label="Table", children=[dcc.Graph(figure=fig_table)])
        ], id='tab-parent', active_tab='tab-chart'
    )
])

app.layout = dbc.Container([
    html.H1('Daily Cases', style={'textAlign': 'center', 'color': colors['background']}),
    app_tabs,
    html.Div(id='tab-content', children=[])
])

@app.callback(
    Output(component_id='tab-content', component_property='children'),
    [Input(component_id='tab-parent', component_property='active_tab')]
)

def switch_tab(tab_chosen):
    if tab_chosen == "tab-chart":
        return chart_layout
    
    elif tab_chosen == "tab-map":
        return fig_map
    # elif tab_chosen == "tab-other":
    #     return other_layout
    return html.P("This shouldn't be displayed for now...")
