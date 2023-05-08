from django.urls import path
from .views import registerPage, loginPage, logoutUser, homePage, detect, SymptomGuidelines, UpdateSymptomGuideline, report_render_pdf_view, UserReportListView, UserReportDelete, AdminReportListView, AdminReportDelete, UpdateDashboardData
from dashboard.plotly_apps.homepage import layout

urlpatterns = [
    path('', homePage, name='home'),
    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('detect/', detect, name='detect'),
    path('symptom-guidelines/', SymptomGuidelines, name='symptom-guidelines'),
    path('update-symptom-guidelines/<str:pk>/', UpdateSymptomGuideline, name='update-symptom-guidelines'),
    path('reports-all/', AdminReportListView, name='reports-all'),
    path('report/<pk>', report_render_pdf_view, name='report_pdf_view'),
    path('reports/', UserReportListView, name='reports'),
    path('report/delete/<pk>', UserReportDelete, name='report-delete'),
    path('report-admin/delete/<pk>', AdminReportDelete, name='report-admin-delete'),
    path('update-dashboard-data/', UpdateDashboardData, name='update-dashboard-data')
]