from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

import pandas as pd

app = DjangoDash('DailyVaccinations', external_stylesheets=[dbc.themes.BOOTSTRAP])


daily_vaccinations = pd.read_csv('dataset/daily_vaccinations.csv')