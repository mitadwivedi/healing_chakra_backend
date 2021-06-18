from django.db import models
from jsonfield import JSONField


# Create your models here.
class LoginCredentials(models.Model):
    username = models.TextField(null=True, blank=True)
    password = models.TextField(null=True, blank=True)


class SignUpCredentials(models.Model):
    username = models.TextField(null=True, blank=True)
    password = models.TextField(null=True, blank=True)
    name = models.TextField(null=True, blank=True)
    email = models.TextField(null=True, blank=True)
    mobile = models.TextField(null=True, blank=True)
    aadhaar = models.TextField(null=True, blank=True)
    location = models.TextField(null=True, blank=True)


class MedicineDonation(models.Model):
    username = models.TextField(null=True, blank=True)
    name = models.TextField(null=True, blank=True)
    mobile = models.TextField(null=True, blank=True)
    aadhaar = models.TextField(null=True, blank=True)
    location = models.TextField(null=True, blank=True)
    medicine_name = models.TextField(null=True, blank=True)
    manufacture_date = models.TextField(null=True, blank=True)
    expiry_date = models.TextField(null=True, blank=True)


class EquipmentDonation(models.Model):
    username = models.TextField(null=True, blank=True)
    name = models.TextField(null=True, blank=True)
    mobile = models.TextField(null=True, blank=True)
    aadhaar = models.TextField(null=True, blank=True)
    location = models.TextField(null=True, blank=True)
    equipment_name = models.TextField(null=True, blank=True)
    manufacture_date = models.TextField(null=True, blank=True)
    expiry_date = models.TextField(null=True, blank=True)