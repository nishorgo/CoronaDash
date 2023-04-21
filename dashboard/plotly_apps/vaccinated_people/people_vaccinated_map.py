import plotly.express as px
import pandas as pd

from dash import html, dcc, dash_table
from dash.dependencies import Input, Output

from .people_vaccinated_app import people_vaccinated

fig_map = px.choropleth(
                    people_vaccinated, 
                    locations="iso_code", 
                    color="people_vaccinated", 
                    hover_name="location", 
                    animation_frame="date", 
                    color_continuous_scale='YlGn',
                    labels={'people_vaccinated': ''},
                    hover_data=['people_vaccinated', 'date'],
                    #range_color=(0, 600000),
                    template='plotly_white'
                )


map_layout = html.Div([
    dcc.Graph(id='fig-map', figure=fig_map)
    
])