from django.urls import path
from .views import registerPage, loginPage, logoutUser, homePage, detect, SymptomGuidelines, UpdateSymptomGuideline, report_render_pdf_view
from dashboard.plotly_apps.homepage import layout

urlpatterns = [
    path('', homePage, name='home'),
    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('detect/', detect, name='detect'),
    path('symptom-guidelines/', SymptomGuidelines, name='symptom-guidelines'),
    path('update-symptom-guidelines/<str:pk>/', UpdateSymptomGuideline, name='update-symptom-guidelines'),
    path('report/<pk>', report_render_pdf_view, name='report_pdf_view'),
]