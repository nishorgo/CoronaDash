from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

import pandas as pd

app = DjangoDash('TotalVaccinationsPerHundred', external_stylesheets=[dbc.themes.BOOTSTRAP])


total_vaccinations_per_hundred = pd.read_csv('dataset/total_vaccinations_per_hundred.csv')