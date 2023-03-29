from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

import pandas as pd

app = DjangoDash('DailyCases', external_stylesheets=[dbc.themes.LUX])

df = pd.read_csv('owid-covid-data.csv')
daily_case = df[['iso_code', 'continent', 'date', 'location', 'new_cases', 'new_cases_smoothed']].copy()