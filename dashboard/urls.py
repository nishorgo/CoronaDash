from django.urls import path
from . import views

from .plotly_apps.confirmed_cases import daily_cases, daily_per_million, total_cases, total_per_million, table
from .plotly_apps.deaths import daily_deaths, daily_deaths_per_million, total_deaths, total_deaths_per_million, table
from .plotly_apps.vaccinations import daily_vaccinations, daily_vaccinations_per_million, total_vaccinations, total_vaccinations_per_hundred, total_boosters, total_boosters_per_hundred, table
from .plotly_apps.vaccinated_people import daily_people_vaccinated, daily_vaccinated_per_hundred, people_fully_vaccinated, people_fully_vaccinated_per_hundred, people_vaccinated, people_vaccinated_per_hundred, table
from .plotly_apps.tests import daily_tests, daily_tests_per_thousand, total_tests, total_tests_per_thousand, positive_rate, tests_per_case, table
from .plotly_apps.hospitalizations import hosp_patients, icu_patients, hosp_patients_per_million, icu_patients_per_million, weekly_hosp_admissions, weekly_icu_admissions, table

urlpatterns = [
    path('confirmed-cases/', views.confirmed_cases, name='confirmed-cases'),
    path('deaths/', views.deaths, name='deaths'),
    path('vaccinations/', views.vaccinations, name='vaccinations'),
    path('vaccinated-people/', views.vaccinated_people, name='vaccinated-people'),
    path('tests/', views.tests, name='tests'),
    path('hospitalizations/', views.hospitalizations, name='hospitalizations'),
]