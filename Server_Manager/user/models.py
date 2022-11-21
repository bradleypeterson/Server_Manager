from django.db import models
from django.contrib.auth.models import AbstractUser

class AppUser(AbstractUser):
    ROLE = (
        ('student', 'student'),
        ('faculty', 'faculty'),
        ('admin', 'admin'),
    )
    role = models.CharField(max_length=100, choices=ROLE, default='student')