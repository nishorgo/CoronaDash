from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

import pandas as pd

app = DjangoDash('WeeklyHospAdmissions', external_stylesheets=[dbc.themes.BOOTSTRAP])


weekly_hosp_admissions = pd.read_csv('dataset/weekly_hosp_admissions.csv')