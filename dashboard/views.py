from django.shortcuts import render
from django.http import JsonResponse

import pandas as pd
import plotly.express as px

def plot(request):
    df = pd.read_csv('owid-covid-data.csv')
    daily_case = df[['date', 'location', 'new_cases', 'new_cases_smoothed']].copy()

    default_country = ['Bangladesh', 'India', 'China', 'United States']

    dff = daily_case[daily_case['location'].isin(default_country)]

    fig = px.line(dff, x='date', y='new_cases_smoothed', color='location', title='Daily Cases',
                    labels={'date': '', 'new_cases_smoothed': '', 'location': 'Country'})

    fig.update_layout(
        font=dict(color='white',size=12,family='Arial',), 
        title=dict(font=dict(size=24)),
        width= 800,
        height= 600,
        plot_bgcolor='black',
        paper_bgcolor='black',
    )

    plot_div = fig.to_html(full_html=False)
    
    return render(request, 'plot.html', {'plot_div':plot_div})