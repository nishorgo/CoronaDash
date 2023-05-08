from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

import pandas as pd

app = DjangoDash('Home', external_stylesheets=[dbc.themes.BOOTSTRAP])


daily_cases = pd.read_csv('dataset/daily_case.csv')
daily_deaths = pd.read_csv('dataset/daily_deaths.csv')
daily_vaccinations = pd.read_csv('dataset/daily_vaccinations.csv')