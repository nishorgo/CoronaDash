import plotly.express as px
import pandas as pd

from dash import html, dcc, dash_table
from dash.dependencies import Input, Output

from .tests_per_case_app import tests_per_case

fig_map = px.choropleth(
                    tests_per_case, 
                    locations="iso_code", 
                    color="tests_per_case", 
                    hover_name="location", 
                    animation_frame="date", 
                    color_continuous_scale='YlGn',
                    labels={'tests_per_case': ''},
                    hover_data=['tests_per_case', 'date'],
                    #range_color=(0, 600000),
                    template='plotly_white'
                )


map_layout = html.Div([
    dcc.Graph(id='fig-map', figure=fig_map)
    
])