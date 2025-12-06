from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_SUPERADMIN = 'superadmin'
    ROLE_ADMIN = 'admin'
    ROLE_USER = 'user'

    ROLE_CHOICES = [
        (ROLE_SUPERADMIN, 'Super Admin'),
        (ROLE_ADMIN, 'Admin'),
        (ROLE_USER, 'User'),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=ROLE_USER,
    )

    def is_superadmin(self):
        return self.role == self.ROLE_SUPERADMIN

    def is_admin(self):
        return self.role == self.ROLE_ADMIN

    def is_basic_user(self):
        return self.role == self.ROLE_USER


class Vehicle(models.Model):
    VEHICLE_TYPE_CHOICES = [
        ('two', 'Two Wheeler'),
        ('three', 'Three Wheeler'),
        ('four', 'Four Wheeler'),
    ]

    vehicle_number = models.CharField(max_length=20, unique=True)
    vehicle_type = models.CharField(max_length=10, choices=VEHICLE_TYPE_CHOICES)
    vehicle_model = models.CharField(max_length=100)
    vehicle_description = models.TextField(blank=True)

    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='vehicles',
    )

    def __str__(self):
        return f"{self.vehicle_number} - {self.vehicle_model}"