from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

import pandas as pd

app = DjangoDash('DailyPeopleVaccinatedPerHundred', external_stylesheets=[dbc.themes.BOOTSTRAP])

df = pd.read_csv('owid-covid-data.csv')
daily_vaccinated_per_hundred = df[['iso_code', 'continent', 'date', 'location', 'new_people_vaccinated_smoothed_per_hundred']].copy()