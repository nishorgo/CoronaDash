from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

import pandas as pd

app = DjangoDash('PositiveRate', external_stylesheets=[dbc.themes.BOOTSTRAP])

df = pd.read_csv('owid-covid-data.csv')
positive_rate = df[['iso_code', 'continent', 'date', 'location', 'positive_rate']].copy()