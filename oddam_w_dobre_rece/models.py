from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from oddam_w_dobre_rece.validators import *

ORGANIZATION_TYPE = [
    ('fundacja', 'fundacja'),
    ('organizacja pozarządowa', 'organizacja pozarządowa'),
    ('zbórka lokalna', 'zbórka lokalna'),
]


class CustomUser(AbstractUser):
    pass

    # def __str__(self):
    #     return self.username


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Institution(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    type = models.CharField(
        max_length=32,
        choices=ORGANIZATION_TYPE,
        default='fundacja'
    )
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class Donation(models.Model):
    quantity = models.PositiveIntegerField()
    categories = models.ManyToManyField(Category, blank=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, blank=True)
    address = models.CharField(max_length=128, validators=[validate_street])
    phone_number = models.CharField(max_length=32, validators=[validate_phone_number])
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=6, validators=[validate_zip_code])
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.CharField(max_length=256)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'Donation no {self.pk}'
