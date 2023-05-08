from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

import pandas as pd

app = DjangoDash('TotalBoostersPerHundred', external_stylesheets=[dbc.themes.BOOTSTRAP])


total_boosters_per_hundred = pd.read_csv('dataset/total_boosters_per_hundred.csv')