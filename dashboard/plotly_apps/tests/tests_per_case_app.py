from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

import pandas as pd

app = DjangoDash('TestsPerCase', external_stylesheets=[dbc.themes.BOOTSTRAP])


tests_per_case = pd.read_csv('dataset/tests_per_case.csv')