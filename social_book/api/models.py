from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.core.validators import FileExtensionValidator


class User(AbstractUser):
    full_name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')], blank=True, null=True)
    credit_card_type = models.CharField(max_length=50, blank=True, null=True)
    credit_card_number = models.CharField(max_length=20, blank=True, null=True)
    cvc = models.CharField(max_length=4, blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)

    public_visibility = models.BooleanField(default=True)
    age = models.IntegerField(blank=True, null=True)
    birth_year = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.birth_year:
            current_year = datetime.now().year
            self.age = current_year - self.birth_year
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.username


class UploadedFile(models.Model):
    TITLE_MAX_LENGTH = 255

    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    description = models.TextField()
    file = models.FileField(upload_to='uploads/', 
                            validators=[FileExtensionValidator(['pdf', 'jpeg', 'jpg'])])
    visibility = models.BooleanField(default=True)  
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    year_published = models.IntegerField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
