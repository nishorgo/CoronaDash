import plotly.express as px
import pandas as pd

from dash import html, dcc, dash_table
from dash.dependencies import Input, Output

from .app import app, daily_case

cc_scale = ['#2b99a1', '#24848b', '#1d7076', '#165d62', '#104a4e', '#0a383c', '#05272a', '#021719', '#010809', '#000101']


fig_map = px.choropleth(
                    daily_case, 
                    locations="iso_code", 
                    color="new_cases_smoothed", 
                    hover_name="location", 
                    animation_frame="date", 
                    color_continuous_scale=cc_scale,
                    labels={'new_cases_smoothed': 'daily cases'},
                    hover_data=['new_cases_smoothed', 'date'],
                    range_color=(0, 600000),
                    template='plotly_white'
                )


map_layout = html.Div([
    dcc.Graph(id='fig-map', figure=fig_map)
])