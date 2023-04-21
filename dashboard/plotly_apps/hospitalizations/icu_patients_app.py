from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

import pandas as pd

app = DjangoDash('ICUPatients', external_stylesheets=[dbc.themes.BOOTSTRAP])

df = pd.read_csv('owid-covid-data.csv')
icu_patients = df[['iso_code', 'continent', 'date', 'location', 'icu_patients']].copy()