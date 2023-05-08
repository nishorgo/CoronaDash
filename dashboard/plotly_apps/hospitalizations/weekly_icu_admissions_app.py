from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

import pandas as pd

app = DjangoDash('WeeklyICUAdmissions', external_stylesheets=[dbc.themes.BOOTSTRAP])


weekly_icu_admissions = pd.read_csv('dataset/weekly_icu_admissions.csv')