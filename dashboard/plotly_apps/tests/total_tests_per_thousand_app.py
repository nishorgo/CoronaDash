from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

import pandas as pd

app = DjangoDash('TotalTestsPerThousand', external_stylesheets=[dbc.themes.BOOTSTRAP])


total_tests_per_thousand = pd.read_csv('dataset/total_tests_per_thousand.csv')