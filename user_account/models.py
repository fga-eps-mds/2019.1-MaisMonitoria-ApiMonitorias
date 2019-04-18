from __future__ import unicode_literals

from django.db import models

class User_account(models.Model):
    user_account_id = models.CharField(primary_key=True, max_length=30)
    
    COURSES = (
        ('SOFTWARE', 'Engenharia de Software'),
        ('ELETRONICA', 'Engenharia Eletronica'),
        ('ENERGIA', 'Engenharia de Energia'),
        ('AERO', 'Engenharia Aeroespacial'),
        ('AUTOMOTIVA', 'Engenharia Automotiva'),
        ('ENGENHARIAS', 'Engenharias'),
    )
    
    course = models.CharField(max_length=11, choices= COURSES)
    description = models.CharField(max_length=500)
    registration_date = models.DateTimeField(auto_now_add=True)
    account_state = models.BooleanField(default=True)

    def __str__(self):
        return self.name