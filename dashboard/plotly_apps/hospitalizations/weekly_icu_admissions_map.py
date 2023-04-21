import plotly.express as px
import pandas as pd

from dash import html, dcc, dash_table
from dash.dependencies import Input, Output

from .weekly_icu_admissions_app import weekly_icu_admissions

fig_map = px.choropleth(
                    weekly_icu_admissions, 
                    locations="iso_code", 
                    color="weekly_icu_admissions", 
                    hover_name="location", 
                    animation_frame="date", 
                    color_continuous_scale='YlGn',
                    labels={'weekly_icu_admissions': ''},
                    hover_data=['weekly_icu_admissions', 'date'],
                    #range_color=(0, 600000),
                    template='plotly_white'
                )


map_layout = html.Div([
    dcc.Graph(id='fig-map', figure=fig_map)
    
])