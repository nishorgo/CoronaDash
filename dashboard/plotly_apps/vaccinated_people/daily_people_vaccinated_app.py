from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

import pandas as pd

app = DjangoDash('DailyPeopleVaccinated', external_stylesheets=[dbc.themes.BOOTSTRAP])

df = pd.read_csv('owid-covid-data.csv')
daily_people_vaccinated = df[['iso_code', 'continent', 'date', 'location', 'new_people_vaccinated_smoothed']].copy()