from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

import pandas as pd

app = DjangoDash('DailyCases', external_stylesheets=[dbc.themes.BOOTSTRAP])

daily_case = pd.read_csv('dataset/daily_case.csv')