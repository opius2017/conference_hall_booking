""" duplicate model
from django.db import models


# Create your models here.
from django.db import models


class Booking(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    programme_title = models.CharField(max_length=100)
    programme_details = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    num_of_participants = models.PositiveIntegerField()
    contact_person = models.CharField(max_length=50)
    contact_email = models.EmailField()
    contact_tel = models.CharField(max_length=15)
    status = models.CharField(max_length=20, default='Pending')
    reason = models.TextField(blank=True, null=True)

    class Meta:
        app_label = 'booking'
"""
