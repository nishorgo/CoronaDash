import plotly.express as px
import pandas as pd

from dash import html, dcc, dash_table
from dash.dependencies import Input, Output

from .positive_rate_app import positive_rate

fig_map = px.choropleth(
                    positive_rate, 
                    locations="iso_code", 
                    color="positive_rate", 
                    hover_name="location", 
                    animation_frame="date", 
                    color_continuous_scale='YlGn',
                    labels={'positive_rate': ''},
                    hover_data=['positive_rate', 'date'],
                    #range_color=(0, 600000),
                    template='plotly_white'
                )


map_layout = html.Div([
    dcc.Graph(id='fig-map', figure=fig_map)
    
])