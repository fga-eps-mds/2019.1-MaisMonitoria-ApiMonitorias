from __future__ import unicode_literals
from django.db import models


# Create your models here.
class InterestArea(models.Model):
    id_interest_area = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)

    
class UserAccount(models.Model):

    user_account_id = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=250)
    photo_url = models.CharField(max_length=150, default="")

    COURSES = (
        ('SOFTWARE', 'Engenharia de Software'),
        ('ELETRONICA', 'Engenharia Eletronica'),
        ('ENERGIA', 'Engenharia de Energia'),
        ('AERO', 'Engenharia Aeroespacial'),
        ('AUTOMOTIVA', 'Engenharia Automotiva'),
        ('ENGENHARIAS', 'Engenharias'),
    )

    monitoring = models.ManyToManyField("tutoring_session.TutoringSession", blank=True)
    monitoring_history = models.ManyToManyField("tutoring_session.Receipt", blank=True)
    interest_areas = models.ManyToManyField(InterestArea, blank=True)

    course = models.CharField(max_length=11, choices=COURSES)
    description = models.CharField(max_length=500, default="")
    registration_date = models.DateTimeField(auto_now_add=True)
    account_state = models.BooleanField(default=True)

