from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

import pandas as pd

app = DjangoDash('TotalBoosters', external_stylesheets=[dbc.themes.BOOTSTRAP])


total_boosters = pd.read_csv('dataset/total_boosters.csv')