from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

import pandas as pd

app = DjangoDash('TotalPerMillion', external_stylesheets=[dbc.themes.BOOTSTRAP])


total_per_million = pd.read_csv('dataset/total_per_million.csv')