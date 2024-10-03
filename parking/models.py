from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import MinValueValidator, MaxValueValidator

class ParkingSpace(models.Model):
    level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    twa = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(50)])
    fwa = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(50)])

    def __str__(self):
        return f"Level {self.level}: {self.twa} TW slots, {self.fwa} FW slots"


class CustomUserManager(BaseUserManager):
    def create_user(self, name, password=None, role='Public', **extra_fields):
        if not name:
            raise ValueError('The Name field must be set')
        user = self.model(name=name, role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, password=None, **extra_fields):
        extra_fields.setdefault('role', 'Admin')
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(name, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255, unique=True)
    role_choices = [
        ("Admin", "Admin"),
        ("Public", "Public"),
    ]
    role = models.CharField(max_length=10, choices=role_choices, default="Public")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['role']

    objects = CustomUserManager()

class ParkingHistory(models.Model):
    level = models.IntegerField(validators=[MinValueValidator(0)])
    type_choices = [
        ('tw', 'Two-Wheeler'),
        ('fw', 'Four-Wheeler'),
    ]
    type = models.CharField(max_length=10, choices=type_choices)
    vehicle_number = models.CharField(max_length=20)
    lot = models.IntegerField(validators=[MinValueValidator(0)])
    fee = models.FloatField(validators=[MinValueValidator(0.0)], null=True, blank=True)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField(null=True, blank=True)
    parking_space = models.ForeignKey(ParkingSpace, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"Parking History for {self.vehicle_number}"
