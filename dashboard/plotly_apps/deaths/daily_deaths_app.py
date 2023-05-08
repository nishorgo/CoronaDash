from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

import pandas as pd

app = DjangoDash('DailyDeaths', external_stylesheets=[dbc.themes.BOOTSTRAP])


daily_deaths = pd.read_csv('dataset/daily_deaths.csv')