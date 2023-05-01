from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

import pandas as pd

app = DjangoDash('Home', external_stylesheets=[dbc.themes.BOOTSTRAP])

df = pd.read_csv('owid-covid-data.csv')
daily_cases = df[[ 'date', 'location', 'new_cases_smoothed']].copy()
daily_deaths = df[['date', 'location', 'new_deaths_smoothed']].copy()
daily_vaccinations = df[['date', 'location', 'new_vaccinations_smoothed']].copy()