from django.contrib import admin
from .models import Questionnaire, SymptomGuideline

# Register your models here.
admin.site.register(Questionnaire)
admin.site.register(SymptomGuideline)