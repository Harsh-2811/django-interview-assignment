from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    role_choice = [
        ('LIBRARIAN','LIBRARIAN'),
        ('MEMBER','MEMBER'),
        ('Admin','Admin'),

        

    ]
    role = models.CharField(max_length=20,choices=role_choice)
    contact_number = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    REQUIRED_FIELDS = ['role','contact_number']
    def __str__(self):
        return self.username
    
