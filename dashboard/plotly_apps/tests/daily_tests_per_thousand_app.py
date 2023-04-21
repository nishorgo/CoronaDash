from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

import pandas as pd

app = DjangoDash('DailyTestsPerThousand', external_stylesheets=[dbc.themes.BOOTSTRAP])

df = pd.read_csv('owid-covid-data.csv')
daily_tests_per_thousand = df[['iso_code', 'continent', 'date', 'location', 'new_tests_per_thousand', 'new_tests_smoothed_per_thousand']].copy()