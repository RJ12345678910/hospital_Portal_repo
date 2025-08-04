from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


USER_TYPE_CHOICES = (
    ('patient', 'Patient'),
    ('doctor', 'Doctor'),
)

class CustomUser(AbstractUser):
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    profile_pic = models.ImageField(upload_to='profiles/', null=True, blank=True)
    address_line1 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    pincode = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f"{self.username} ({self.user_type})"

class DoctorVerification(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    medical_license_number = models.CharField(max_length=50)
    college_name = models.CharField(max_length=255)
    degree = models.CharField(max_length=100)
    degree_photo = models.ImageField(upload_to='degree_photos/', blank=True, null=True)
    phone_number1 = models.CharField(max_length=15)
    phone_number2 = models.CharField(max_length=15)
    govt_id_photo = models.ImageField(upload_to='govt_ids/', blank=True, null=True)
    verified = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Verification for Dr. {self.user.get_full_name()}"