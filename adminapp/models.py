from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from patient.models import Patient




class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group, related_name="customuser_set", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_set", blank=True)

    def __str__(self):
        return self.username




class Facility(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    departments = models.TextField(help_text="List departments separated by commas")

    def __str__(self):
        return self.name






