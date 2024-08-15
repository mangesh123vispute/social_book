from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    full_name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')], blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    credit_card_type = models.CharField(max_length=50, blank=True, null=True)
    credit_card_number = models.CharField(max_length=20, blank=True, null=True)
    cvc = models.CharField(max_length=4, blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username
