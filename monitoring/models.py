from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Monitoring(models.Model):
    id_monitoring = models.AutoField(primary_key=True)
    name_monitoring = models.CharField(max_length=150)
    matter = models.CharField(max_length=200)
    description = models.CharField(max_length=500, default="")
    # applicants
    # applicants_accepted
    status_monitoring = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True) 
    