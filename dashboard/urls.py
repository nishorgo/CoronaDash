from django.urls import path
from . import views

from .plotly_apps.confirmed_cases import daily_cases, daily_per_million, total_cases, total_per_million, table
from .plotly_apps.deaths import daily_deaths, daily_deaths_per_million, total_deaths, total_deaths_per_million, table
from .plotly_apps.vaccinations import daily_vaccinations, daily_vaccinations_per_million, total_vaccinations, total_vaccinations_per_hundred, total_boosters, total_boosters_per_hundred, table
from .plotly_apps.vaccinated_people import daily_people_vaccinated, daily_vaccinated_per_hundred, people_fully_vaccinated, people_fully_vaccinated_per_hundred, people_vaccinated, people_vaccinated_per_hundred, table

urlpatterns = [
    path('', views.confirmed_cases, name='confirmed-cases'),
    path('deaths/', views.deaths, name='deaths'),
    path('vaccinations/', views.vaccinations, name='vaccinations'),
    path('vaccinated-people/', views.vaccinated_people, name='vaccinated-people'),
]