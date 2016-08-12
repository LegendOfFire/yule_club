from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


# Create your models here.
class Member(models.Model):
    user_name = models.CharField("Name", max_length=64)
    email = models.EmailField("E-mail")
#   login_status = models.BooleanField("Login Status", default=False)
#   reg_date = models.DateTimeField("Registration Date")
#   last_login_time = models.DateTimeField("Last Login Time")

    def __str__(self):
        return "Member"
