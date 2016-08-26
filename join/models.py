from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Member(models.Model):
    user_name = models.CharField("Name", max_length=64)
    email_addr = models.EmailField("E-mail")
#    password = models.CharField("Password", max_length=16)
    reg_date = models.DateTimeField("Registration Date")
    is_joined = models.BooleanField("Join or Not")
    join_times = models.IntegerField("Join Times")
    is_leader = models.BooleanField("Leader Role", default=False)

    def __str__(self):
        return "Member List"


class Enrollment(models.Model):
    week_num = models.IntegerField("Week Number", unique=True)
    counts = models.IntegerField("Enrollment Number", default=0)
    status = models.BooleanField("Open for Enrollment", default=True)

    def __str__(self):
        return "Enrollment History"
