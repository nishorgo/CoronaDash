import plotly.express as px
import pandas as pd

from dash import html, dcc, dash_table
from dash.dependencies import Input, Output

from .total_tests_per_thousand_app import total_tests_per_thousand

fig_map = px.choropleth(
                    total_tests_per_thousand, 
                    locations="iso_code", 
                    color="total_tests_per_thousand", 
                    hover_name="location", 
                    animation_frame="date", 
                    color_continuous_scale='YlGn',
                    labels={'total_tests_per_thousand': ''},
                    hover_data=['total_tests_per_thousand', 'date'],
                    #range_color=(0, 600000),
                    template='plotly_white'
                )


map_layout = html.Div([
    dcc.Graph(id='fig-map', figure=fig_map)
    
])