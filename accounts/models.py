from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser): 
    age = models.PositiveBigIntegerField(null=True, blank=True)
    def __str__(self):
        return self.username

# Create your models here.
