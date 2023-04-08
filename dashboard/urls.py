from django.urls import path
from . import views

from .plotly_apps import daily_cases, table, test

urlpatterns = [
    path('', views.plot, name='plot'),
]