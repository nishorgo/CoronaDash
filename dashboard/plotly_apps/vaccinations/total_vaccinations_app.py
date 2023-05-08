from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

import pandas as pd

app = DjangoDash('TotalVaccinations', external_stylesheets=[dbc.themes.BOOTSTRAP])


total_vaccinations = pd.read_csv('dataset/total_vaccinations.csv')