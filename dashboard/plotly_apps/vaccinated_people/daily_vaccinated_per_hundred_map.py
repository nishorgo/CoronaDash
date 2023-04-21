import plotly.express as px
import pandas as pd

from dash import html, dcc, dash_table
from dash.dependencies import Input, Output

from .daily_vaccinated_per_hundred_app import daily_vaccinated_per_hundred

fig_map = px.choropleth(
                    daily_vaccinated_per_hundred, 
                    locations="iso_code", 
                    color="new_people_vaccinated_smoothed_per_hundred", 
                    hover_name="location", 
                    animation_frame="date", 
                    color_continuous_scale='YlGn',
                    labels={'new_people_vaccinated_smoothed_per_hundred': ''},
                    hover_data=['new_people_vaccinated_smoothed_per_hundred', 'date'],
                    #range_color=(0, 600000),
                    template='plotly_white'
                )


map_layout = html.Div([
    dcc.Graph(id='fig-map', figure=fig_map)
    
])