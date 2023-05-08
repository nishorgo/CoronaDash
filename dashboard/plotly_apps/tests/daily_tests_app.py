from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

import pandas as pd

app = DjangoDash('DailyTests', external_stylesheets=[dbc.themes.BOOTSTRAP])


daily_tests = pd.read_csv('dataset/daily_tests.csv')