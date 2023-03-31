from django.urls import path
from . import views

from .plotly_apps import daily_cases, table, multi_outs

urlpatterns = [
    path('', views.plot, name='plot'),
]