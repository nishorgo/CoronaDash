from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

import pandas as pd

app = DjangoDash('ICUPatientsPerMillion', external_stylesheets=[dbc.themes.BOOTSTRAP])


icu_patients_per_million = pd.read_csv('dataset/icu_patients_per_million.csv')