import plotly.express as px
import pandas as pd

from dash import html, dcc, dash_table
from dash.dependencies import Input, Output

from .hosp_patients_app import hosp_patients

fig_map = px.choropleth(
                    hosp_patients, 
                    locations="iso_code", 
                    color="hosp_patients", 
                    hover_name="location", 
                    animation_frame="date", 
                    color_continuous_scale='YlGn',
                    labels={'hosp_patients': ''},
                    hover_data=['hosp_patients', 'date'],
                    #range_color=(0, 600000),
                    template='plotly_white'
                )


map_layout = html.Div([
    dcc.Graph(id='fig-map', figure=fig_map)
    
])