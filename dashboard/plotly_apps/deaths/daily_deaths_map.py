import plotly.express as px
import pandas as pd

from dash import html, dcc, dash_table
from dash.dependencies import Input, Output

from .daily_deaths_app import daily_deaths

fig_map = px.choropleth(
                    daily_deaths, 
                    locations="iso_code", 
                    color="new_deaths", 
                    hover_name="location", 
                    animation_frame="date", 
                    color_continuous_scale='YlGn',
                    labels={'new_deaths': ''},
                    hover_data=['new_deaths', 'date'],
                    #range_color=(0, 600000),
                    template='plotly_white'
                )


map_layout = html.Div([
    dcc.Graph(id='fig-map', figure=fig_map)
    
])