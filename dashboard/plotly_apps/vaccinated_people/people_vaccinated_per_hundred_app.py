from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

import pandas as pd

app = DjangoDash('PeopleVaccinatedPerHundred', external_stylesheets=[dbc.themes.BOOTSTRAP])


people_vaccinated_per_hundred = pd.read_csv('dataset/people_vaccinated_per_hundred.csv')