from __future__ import unicode_literals
from django.db import models
from user_account.models import UserAccount

class Solicitation(models.Model):
    status_solicitation = models.BooleanField(default = True)
    resquester = models.ManyToManyField(UserAccount)
    create_date = models.DateTimeField(auto_now_add = True)

class TutoringSession(models.Model):
    id_tutoring_session = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    subject = models.CharField(max_length=200)
    description = models.CharField(max_length=500, default="")
    applicants = models.ManyToManyField(Solicitation)
    #accepted_applicants = models.ManyToManyField(Solicitation)
    status_tutoring_session = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)

class Receipt(models.Model):
    id_receipt = models.AutoField(primary_key=True)
    accomplished = models.BooleanField(default=True)
    issue_date = models.DateTimeField(auto_now_add=True)