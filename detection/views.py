from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.template.loader import get_template
from django.contrib import messages
from django.http import HttpResponse

from .forms import CreateUserForm, QuestionnaireForm, UpdateSymptomGuidelineForm
from .models import SymptomGuideline, Questionnaire

from xhtml2pdf import pisa
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


@login_required(login_url='login')
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

            guidelines = SymptomGuideline.objects.all()
            
            questionnaire.save()
            return render (request, 'detection/result.html', {'questionnaire': questionnaire, 'guidelines': guidelines})
        
    else:
        form = QuestionnaireForm()
        return render(request, 'detection/questionnaire.html', {'form': form})
    

@staff_member_required(login_url='home')
def SymptomGuidelines(request):
    symptoms = SymptomGuideline.objects.all()
    return render(request, 'detection/symptom_guidelines.html', {'symptoms': symptoms})


@staff_member_required(login_url='home')
def UpdateSymptomGuideline(request, pk):
    symptom_object = get_object_or_404(SymptomGuideline, pk=pk)
    form = UpdateSymptomGuidelineForm(instance=symptom_object)
    if request.method == 'POST':
        form = UpdateSymptomGuidelineForm(request.POST, instance=symptom_object)
        if form.is_valid():
            form.save()
            return redirect('symptom-guidelines')
        
    return render(request, 'detection/update_symptom_guideline.html', {'form': form, 'symptom_name':symptom_object.display_name})


def report_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    report = get_object_or_404(Questionnaire, pk=pk)

    guidelines = SymptomGuideline.objects.all()
    template_path = 'detection/generate_pdf.html'
    context = {'report': report, 'guidelines': guidelines}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'filename="report.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    
    return response