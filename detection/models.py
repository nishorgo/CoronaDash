from django.db import models
from django.contrib.auth.models import User


class Questionnaire(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)

    breathing_problem = models.BooleanField(blank=False, null=False)
    fever = models.BooleanField(blank=False, null=False)
    dry_cough = models.BooleanField(blank=False, null=False)
    sore_throat = models.BooleanField(blank=False, null=False)
    runny_nose = models.BooleanField(blank=False, null=False)
    asthma = models.BooleanField(blank=False, null=False)
    chronic_lung_disease = models.BooleanField(blank=False, null=False)
    headache = models.BooleanField(blank=False, null=False)
    heart_disease = models.BooleanField(blank=False, null=False)
    diabetes = models.BooleanField(blank=False, null=False)
    hypertension = models.BooleanField(blank=False, null=False)
    fatigue = models.BooleanField(blank=False, null=False)
    gastrointestinal = models.BooleanField(blank=False, null=False)
    abroad_travel = models.BooleanField(blank=False, null=False)
    contact_with_covid_patient = models.BooleanField(blank=False, null=False)
    attended_large_gathering = models.BooleanField(blank=False, null=False)
    visited_public_exposed_places = models.BooleanField(blank=False, null=False)
    family_working_in_public_exposed_places = models.BooleanField(blank=False, null=False)
    wearing_mask = models.BooleanField(blank=False, null=False)
    sanitization_from_market = models.BooleanField(blank=False, null=False)
    covid = models.BooleanField(blank=False, null=False)

    def __str__(self):
        return self.patient.username + ' ' + str(self.date_time)

