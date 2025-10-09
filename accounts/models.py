from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=False)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    location = models.CharField(max_length=20, blank=True, null=True)
    language = models.CharField(max_length=10,blank=True, null=True)
    currency = models.CharField(max_length=3, blank = True, null=True)

