from enum import unique
from tkinter import CASCADE
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from prison.models import *
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField 

class User(AbstractUser):
    
    is_Admin = models.BooleanField(default=False)
    is_Manager = models.BooleanField(default=False)
    is_DataEncoder = models.BooleanField(default=False)
    is_SuperManager=models.BooleanField(default=False)
    phone = PhoneNumberField(unique = True, null = False, blank = False) # Here
    address = models.CharField(max_length=255,blank=True,null=True)
    email = models.EmailField(blank=True,null=True, unique=True) 
    prison=models.ForeignKey(Prison, null=True, on_delete= models.SET_NULL,blank=True) 