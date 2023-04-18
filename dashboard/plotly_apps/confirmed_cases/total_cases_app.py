from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

import pandas as pd

app = DjangoDash('TotalCases', external_stylesheets=[dbc.themes.LUX])

df = pd.read_csv('owid-covid-data.csv')
total_cases = df[['iso_code', 'continent', 'date', 'location', 'total_cases']].copy()