from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

import pandas as pd

app = DjangoDash('DailyPeopleVaccinated', external_stylesheets=[dbc.themes.BOOTSTRAP])


daily_people_vaccinated = pd.read_csv('dataset/daily_people_vaccinated.csv')