from django.shortcuts import render

import pandas as pd
import plotly.express as px

def confirmed_cases(request):
    return render(request, 'dashboard/confirmed_cases.html')


def deaths(request):
    return render(request, 'dashboard/deaths.html')


def vaccinations(request):
    return render(request, 'dashboard/vaccinations.html')


def vaccinated_people(request):
    return render(request, 'dashboard/vaccinated_people.html')


def tests(request):
    return render(request, 'dashboard/tests.html')