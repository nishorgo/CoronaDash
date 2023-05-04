from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm, QuestionnaireForm
import numpy as np
import pandas as pd
import joblib


def homePage(request):
    df = pd.read_csv('owid-covid-data.csv')
    country = 'World'
    most_recent_date = df.loc[df['location'] == country, 'date'].max()
    row = df.loc[(df['location'] == country) & (df['date'] == most_recent_date)]
    cases = row.loc[:, 'total_cases'].values[0]
    deaths = row.loc[:, 'total_deaths'].values[0]
    vaccinations = row.loc[:, 'people_vaccinated'].values[0]
    context = {'cases': int(cases), 'deaths': int(deaths), 'vaccinations': int(vaccinations)}
    return render(request, 'detection/home.html', context)


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()

                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')

        context = {'form': form}
        return render(request, 'detection/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'detection/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def detect(request):
    if request.method == 'POST':
        form = QuestionnaireForm(request.POST)
        if form.is_valid():
            questionnaire = form.save(commit=False)
            questionnaire.patient = request.user

            model = joblib.load('detection/model.pkl')
            patient_input = np.array([questionnaire.breathing_problem, questionnaire.fever, questionnaire.dry_cough, 
                                       questionnaire.sore_throat, questionnaire.runny_nose, questionnaire.asthma, 
                                       questionnaire.chronic_lung_disease, questionnaire.headache, questionnaire.heart_disease, 
                                       questionnaire.diabetes, questionnaire.hypertension, questionnaire.fatigue, 
                                       questionnaire.gastrointestinal, questionnaire.abroad_travel, questionnaire.contact_with_covid_patient, 
                                       questionnaire.attended_large_gathering, questionnaire.visited_public_exposed_places, 
                                       questionnaire.family_working_in_public_exposed_places, questionnaire.wearing_mask, 
                                       questionnaire.sanitization_from_market])
            patient_input = patient_input.reshape(1, -1)
            questionnaire.covid = model.predict(patient_input)[0]
            
            questionnaire.save()
            return render (request, 'detection/result.html', {'questionnaire': questionnaire})
        
    else:
        form = QuestionnaireForm()
        return render(request, 'detection/questionnaire.html', {'form': form})