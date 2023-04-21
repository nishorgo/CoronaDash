from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

import pandas as pd

app = DjangoDash('TotalVaccinations', external_stylesheets=[dbc.themes.BOOTSTRAP])

df = pd.read_csv('owid-covid-data.csv')
total_vaccinations = df[['iso_code', 'continent', 'date', 'location', 'total_vaccinations']].copy()