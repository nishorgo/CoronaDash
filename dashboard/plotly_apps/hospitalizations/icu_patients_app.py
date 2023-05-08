from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

import pandas as pd

app = DjangoDash('ICUPatients', external_stylesheets=[dbc.themes.BOOTSTRAP])

icu_patients = pd.read_csv('dataset/icu_patients.csv')