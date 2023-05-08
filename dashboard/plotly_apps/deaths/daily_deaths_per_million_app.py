from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

import pandas as pd

app = DjangoDash('DailyDeathsPerMillion', external_stylesheets=[dbc.themes.BOOTSTRAP])


daily_deaths_per_million = pd.read_csv('dataset/daily_deaths_per_million.csv')