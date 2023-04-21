import plotly.express as px
import pandas as pd

from dash import html, dcc, dash_table
from dash.dependencies import Input, Output

from .icu_patients_per_million_app import icu_patients_per_million

fig_map = px.choropleth(
                    icu_patients_per_million, 
                    locations="iso_code", 
                    color="icu_patients_per_million", 
                    hover_name="location", 
                    animation_frame="date", 
                    color_continuous_scale='YlGn',
                    labels={'icu_patients_per_million': ''},
                    hover_data=['icu_patients_per_million', 'date'],
                    #range_color=(0, 600000),
                    template='plotly_white'
                )


map_layout = html.Div([
    dcc.Graph(id='fig-map', figure=fig_map)
    
])