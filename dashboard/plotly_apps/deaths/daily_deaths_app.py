from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

import pandas as pd

app = DjangoDash('DailyDeaths', external_stylesheets=[dbc.themes.BOOTSTRAP])

df = pd.read_csv('owid-covid-data.csv')
daily_deaths = df[['iso_code', 'continent', 'date', 'location', 'new_deaths', 'new_deaths_smoothed']].copy()