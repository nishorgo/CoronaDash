from django.shortcuts import render
from django.http import JsonResponse

import pandas as pd
import plotly.express as px

def plot(request):
    
    return render(request, 'plot.html')

