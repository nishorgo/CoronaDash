from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

import pandas as pd

app = DjangoDash('WeeklyICUAdmissions', external_stylesheets=[dbc.themes.BOOTSTRAP])

df = pd.read_csv('owid-covid-data.csv')
weekly_icu_admissions = df[['iso_code', 'continent', 'date', 'location', 'weekly_icu_admissions']].copy()