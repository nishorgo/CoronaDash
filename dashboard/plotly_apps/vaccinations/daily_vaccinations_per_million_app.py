from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

import pandas as pd

app = DjangoDash('DailyVaccinationsPerMillion', external_stylesheets=[dbc.themes.BOOTSTRAP])

df = pd.read_csv('owid-covid-data.csv')
daily_vaccinations_per_million = df[['iso_code', 'continent', 'date', 'location', 'new_vaccinations_smoothed_per_million']].copy()