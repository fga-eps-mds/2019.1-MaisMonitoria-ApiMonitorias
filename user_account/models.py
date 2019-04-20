from __future__ import unicode_literals

from django.db import models

# Create your models here.

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
    
    # monitoring = models.ManyToManyField(Monitoring)
    # monitoring_history = models.ManyToManyField(Receipt)
    # interest_areas = models.ManyToManyField(InterestArea)
    
    course = models.CharField(max_length=11, choices=COURSES)
    description = models.CharField(max_length=500, default="")
    registration_date = models.DateTimeField(auto_now_add=True)
    account_state = models.BooleanField(default=True)

    def __str__(self):
        return self.name