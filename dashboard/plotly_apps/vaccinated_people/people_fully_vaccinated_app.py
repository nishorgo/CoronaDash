from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

import pandas as pd

app = DjangoDash('PeopleFullyVaccinated', external_stylesheets=[dbc.themes.BOOTSTRAP])


people_fully_vaccinated = pd.read_csv('dataset/people_fully_vaccinated.csv')