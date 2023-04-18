import plotly.express as px
import pandas as pd

from dash import html, dcc, dash_table
from dash.dependencies import Input, Output

from .daily_per_million_app import daily_per_million

fig_map = px.choropleth(
                    daily_per_million, 
                    locations="iso_code", 
                    color="new_cases_smoothed_per_million", 
                    hover_name="location", 
                    animation_frame="date", 
                    color_continuous_scale='YlGn',
                    labels={'new_cases_smoothed_per_million': 'daily cases per million'},
                    hover_data=['new_cases_smoothed_per_million', 'date'],
                    #range_color=(0, 600000),
                    template='plotly_white'
                )


map_layout = html.Div([
    dcc.Graph(id='fig-map', figure=fig_map)
    
])