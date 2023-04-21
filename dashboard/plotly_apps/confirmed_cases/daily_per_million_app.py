from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

import pandas as pd

app = DjangoDash('DailyPerMillion', external_stylesheets=[dbc.themes.BOOTSTRAP])

df = pd.read_csv('owid-covid-data.csv')
daily_per_million = df[['iso_code', 'continent', 'date', 'location', 'new_cases_per_million', 'new_cases_smoothed_per_million']].copy()