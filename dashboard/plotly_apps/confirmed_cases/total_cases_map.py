import plotly.express as px
import pandas as pd

from dash import html, dcc, dash_table
from dash.dependencies import Input, Output

from .total_cases_app import total_cases

fig_map = px.choropleth(
                    total_cases, 
                    locations="iso_code", 
                    color="total_cases", 
                    hover_name="location", 
                    animation_frame="date", 
                    color_continuous_scale='YlGn',
                    labels={'total_cases': ''},
                    hover_data=['total_cases', 'date'],
                    template='plotly_white'
                )


map_layout = html.Div([
    dcc.Graph(id='fig-map', figure=fig_map)
    
])