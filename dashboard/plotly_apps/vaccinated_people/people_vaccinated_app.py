from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

import pandas as pd

app = DjangoDash('PeopleVaccinated', external_stylesheets=[dbc.themes.BOOTSTRAP])

df = pd.read_csv('owid-covid-data.csv')
people_vaccinated = df[['iso_code', 'continent', 'date', 'location', 'people_vaccinated']].copy()