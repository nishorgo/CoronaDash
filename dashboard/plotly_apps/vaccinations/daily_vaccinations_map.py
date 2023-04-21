import plotly.express as px
import pandas as pd

from dash import html, dcc, dash_table
from dash.dependencies import Input, Output

from .daily_vaccinations_app import daily_vaccinations

fig_map = px.choropleth(
                    daily_vaccinations, 
                    locations="iso_code", 
                    color="new_vaccinations", 
                    hover_name="location", 
                    animation_frame="date", 
                    color_continuous_scale='YlGn',
                    labels={'new_vaccinations': ''},
                    hover_data=['new_vaccinations', 'date'],
                    #range_color=(0, 600000),
                    template='plotly_white'
                )


map_layout = html.Div([
    dcc.Graph(id='fig-map', figure=fig_map)
    
])