from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

import pandas as pd

app = DjangoDash('DailyPeopleVaccinatedPerHundred', external_stylesheets=[dbc.themes.BOOTSTRAP])


daily_vaccinated_per_hundred = pd.read_csv('dataset/daily_vaccinated_per_hundred.csv')