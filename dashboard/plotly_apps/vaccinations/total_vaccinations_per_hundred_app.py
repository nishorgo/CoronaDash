from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

import pandas as pd

app = DjangoDash('TotalVaccinationsPerHundred', external_stylesheets=[dbc.themes.BOOTSTRAP])

df = pd.read_csv('owid-covid-data.csv')
total_vaccinations_per_hundred = df[['iso_code', 'continent', 'date', 'location', 'total_vaccinations_per_hundred']].copy()