from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

import pandas as pd

app = DjangoDash('TestsPerCase', external_stylesheets=[dbc.themes.BOOTSTRAP])

df = pd.read_csv('owid-covid-data.csv')
tests_per_case = df[['iso_code', 'continent', 'date', 'location', 'tests_per_case']].copy()