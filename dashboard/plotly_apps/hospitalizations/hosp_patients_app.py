from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

import pandas as pd

app = DjangoDash('HospPatients', external_stylesheets=[dbc.themes.BOOTSTRAP])


hosp_patients = pd.read_csv('dataset/hosp_patients.csv')