from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

import pandas as pd

app = DjangoDash('TotalDeathsPerMillion', external_stylesheets=[dbc.themes.BOOTSTRAP])


total_deaths_per_million = pd.read_csv('dataset/total_deaths_per_million.csv')