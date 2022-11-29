from django.db import models
from django.contrib.auth.models import AbstractUser 

class User(AbstractUser):

    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")

    first_name = models.CharField(max_length=150,
    editable=False)
    last_name = models.CharField(max_length=150,
    editable=False)
    avatar = models.ImageField(default=False)
    name = models.CharField(max_length=15, default=False)
    is_host = models.BooleanField(default=False)
    gender = models.CharField(max_length=10, choices=GenderChoices.choices,default=False)
    pass

# Create your models here.