import plotly.express as px
import pandas as pd

from dash import html, dcc, dash_table
from dash.dependencies import Input, Output

from .weekly_hosp_admissions_app import weekly_hosp_admissions

fig_map = px.choropleth(
                    weekly_hosp_admissions, 
                    locations="iso_code", 
                    color="weekly_hosp_admissions", 
                    hover_name="location", 
                    animation_frame="date", 
                    color_continuous_scale='YlGn',
                    labels={'weekly_hosp_admissions': ''},
                    hover_data=['weekly_hosp_admissions', 'date'],
                    #range_color=(0, 600000),
                    template='plotly_white'
                )


map_layout = html.Div([
    dcc.Graph(id='fig-map', figure=fig_map)
    
])