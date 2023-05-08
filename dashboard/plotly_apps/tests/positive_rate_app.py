from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

import pandas as pd

app = DjangoDash('PositiveRate', external_stylesheets=[dbc.themes.BOOTSTRAP])


positive_rate = pd.read_csv('dataset/positive_rate.csv')