from sre_constants import MAX_UNTIL
from tkinter import CASCADE, Image
from turtle import width
from winreg import SaveKey
from django.db import models
from account.models import User 
from django.forms import DateTimeField
from django.contrib.auth.models import AbstractUser
from prison.models import *
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
   
    
# class Crime(models.Model): 
#     CrimeName=models.CharField(max_length=100)
#     Discription=models.CharField(max_length=200) 
#     createdby = models.ForeignKey(User, null=True,on_delete=models.CASCADE)
#     def __str__(self):
#         return self.CrimeName

cat_choice=(
    ("Criteria1","Criteria1"),
    ("Criteria2","Criteria2")
)

class Criminal(models.Model):
     
    CriminalName=models.CharField(max_length=200, null=True)
    Age=models.PositiveIntegerField( null=True)
    Height=models.FloatField( validators=[MinValueValidator(1), MaxValueValidator(2.5)],null=True)
    EyeColor=models.CharField(max_length=100,null=True) 
    Gender=models.CharField(max_length=8,null=True)  
    Nationality=models.CharField(max_length=100,null=True)
    EntranceDate=models.DateField(auto_now=True,null=True)
    ReleasedDate=models.DateField(null=True)
    timeleft=models.CharField(max_length=100,null=True)
    Guardian=models.CharField(max_length=100,null=True)
    Bloodtype=models.CharField(max_length=30,null=True)
    AssignedCellNumber=models.PositiveIntegerField(null=True)
    Status= models.BooleanField(default=True)
    ImprisonmentTime=models.PositiveIntegerField(null=True) 
    Address=models.CharField(max_length=100,null=True) 
    Category=models.CharField(max_length=20, null=True, choices=cat_choice, blank=True)
    CrimeDescription=models.TextField(max_length=200, null=True, blank=True)
    prison=models.ForeignKey(Prison,on_delete=models.CASCADE ,null=True)
    createdby = models.ForeignKey(User,null=True ,on_delete=models.CASCADE)
    
    # timeleft=ReleasedDate - EntranceDate
    # print ({{timeleft.days}})
    # print((ReleasedDate - EntranceDate).days)

    def timeleft(self, *args, **kwargs):
        self.timeleft=(self.ReleasedDate - self.EntranceDate)
        super().save(*args, **kwargs)
    
        return self.timeleft
    
    # @property
    # def timeleft(self):
    #     return(self.ReleasedDate - self.EntranceDate)

    def __str__(self):
        return self.CriminalName


    

class Visitor(models.Model): 
    Name=models.CharField(max_length=200,null=True)
    Gender=models.CharField(max_length=8 ,null=True )
    Address=models.CharField(max_length=200,null=True)
    Nationality=models.CharField(max_length=200,null=True)
    VisitDate=models.DateField(auto_now=True)
    VisitedCriminal=models.ForeignKey(Criminal, null=True, on_delete= models.SET_NULL)
    createdby = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    prison=models.ForeignKey(Prison,on_delete=models.CASCADE ,null=True)
    
    def __str__(self):
        return self.Name


