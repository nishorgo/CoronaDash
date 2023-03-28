from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

app = DjangoDash('DailyCases', external_stylesheets=[dbc.themes.LUX])