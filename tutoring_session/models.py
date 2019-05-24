from __future__ import unicode_literals
from django.db import models
from user_account.models import UserAccount


class TutoringSession(models.Model):
    id_tutoring_session = models.AutoField(primary_key=True)
    monitor= models.ForeignKey("user_account.UserAccount", on_delete=models.CASCADE, related_name='monitor')
    name = models.CharField(max_length=150)
    subject = models.CharField(max_length=200)
    description = models.CharField(max_length=500, default="")
    status_tutoring_session = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    
