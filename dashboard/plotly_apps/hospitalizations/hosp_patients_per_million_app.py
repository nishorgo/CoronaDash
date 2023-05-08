from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

import pandas as pd

app = DjangoDash('HospPatientsPerMillion', external_stylesheets=[dbc.themes.BOOTSTRAP])

hosp_patients_per_million = pd.read_csv('dataset/hosp_patients_per_million.csv')