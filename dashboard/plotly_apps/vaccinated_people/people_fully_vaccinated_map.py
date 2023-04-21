import plotly.express as px
import pandas as pd

from dash import html, dcc, dash_table
from dash.dependencies import Input, Output

from .people_fully_vaccinated_app import people_fully_vaccinated

fig_map = px.choropleth(
                    people_fully_vaccinated, 
                    locations="iso_code", 
                    color="people_fully_vaccinated", 
                    hover_name="location", 
                    animation_frame="date", 
                    color_continuous_scale='YlGn',
                    labels={'people_fully_vaccinated': ''},
                    hover_data=['people_fully_vaccinated', 'date'],
                    #range_color=(0, 600000),
                    template='plotly_white'
                )


map_layout = html.Div([
    dcc.Graph(id='fig-map', figure=fig_map)
    
])