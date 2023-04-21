from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

import pandas as pd

app = DjangoDash('TotalDeathsPerMillion', external_stylesheets=[dbc.themes.BOOTSTRAP])

df = pd.read_csv('owid-covid-data.csv')
total_deaths_per_million = df[['iso_code', 'continent', 'date', 'location', 'total_deaths_per_million']].copy()