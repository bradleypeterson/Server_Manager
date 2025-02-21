from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class AppUser(AbstractUser):
    ROLE = (
        ('faculty', 'faculty'),
        ('admin', 'admin'),
        ('student', 'student'),
    )
    role = models.CharField(max_length=100, choices=ROLE, default='faculty')
