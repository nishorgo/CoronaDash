from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

import pandas as pd

app = DjangoDash('DailyTests', external_stylesheets=[dbc.themes.BOOTSTRAP])

df = pd.read_csv('owid-covid-data.csv')
daily_tests = df[['iso_code', 'continent', 'date', 'location', 'new_tests', 'new_tests_smoothed']].copy()