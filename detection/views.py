from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.template.loader import get_template
from django.contrib import messages
from django.http import HttpResponse

from .forms import CreateUserForm, QuestionnaireForm, UpdateSymptomGuidelineForm
from .models import SymptomGuideline, Questionnaire
from .utils import SeparateDataframes, FindHomePageData

from xhtml2pdf import pisa
import numpy as np
import pandas as pd
import joblib
import requests
import os


def homePage(request):
    data_tuple = joblib.load('dataset/total_numbers.joblib')
    cases, deaths, vaccinations = data_tuple
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


@login_required(login_url='login')
def report_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    report = get_object_or_404(Questionnaire, pk=pk)

    guidelines = SymptomGuideline.objects.all()
    template_path = 'detection/generate_pdf.html'
    context = {'report':report, 'guidelines':guidelines}

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'filename="report.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    
    return response


@login_required(login_url='login')
def UserReportListView(request):
    current_username = request.user.username
    current_user_id = request.user.id
    current_user_reports = Questionnaire.objects.filter(patient=current_user_id).order_by('-date_time')
    return render(request, 'detection/reports.html', {'current_user_reports':current_user_reports, 'current_username':current_username})


@login_required(login_url='login')
def UserReportDelete(request, pk):
    report = get_object_or_404(Questionnaire, pk=pk)

    if request.method == 'POST':
        report.delete()
        return redirect('reports')
    
    return render(request, 'detection/delete_report.html', {'report':report})





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


@staff_member_required(login_url='home')
def AdminReportListView(request):
    reports = Questionnaire.objects.all().order_by('-date_time')
    return render(request, 'detection/reports_all.html', {'reports':reports})


@staff_member_required(login_url='home')
def AdminReportDelete(request, pk):
    report = get_object_or_404(Questionnaire, pk=pk)

    if request.method == 'POST':
        report.delete()
        return redirect('reports-all')
    
    return render(request, 'detection/admin_delete_report.html', {'report':report})


@staff_member_required(login_url='home')
def UpdateDashboardData(request):
    # URL of the raw CSV file on GitHub
    url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
    folder_name = "dataset"
    file_name = "owid-covid-data.csv"

    # Create a folder named "dataset" if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Set the file path to "dataset/filename.csv"
    file_path = os.path.join(folder_name, file_name)

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Write the contents of the response to the file
        with open(file_path, "wb") as f:
            f.write(response.content)
            download_success = True
    else:
        download_success = False
        return render(request, 'detection/update_dashboard_data.html', {'download_success':download_success})

    print('Download Success: ', download_success)

    separate_dataframe_instances = False

    print('Separate Dataframe Instances: Start')

    FindHomePageData()
    print('Find Home Page Data Done')
    SeparateDataframes()

    separate_dataframe_instances = True
    print('Separate Dataframe Instances: ', separate_dataframe_instances)
    context = {'download_success':download_success, 'separate_dataframe_instances':separate_dataframe_instances}


    return render(request, 'detection/update_dashboard_data.html', context)