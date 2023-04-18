from django.urls import path
from . import views

from .plotly_apps.confirmed_cases import daily_cases, daily_per_million, total_cases, total_per_million, table

urlpatterns = [
    path('', views.plot, name='plot'),
]