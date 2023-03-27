from dataclasses import field
from select import select
from tkinter import Widget
from unittest.util import _MAX_LENGTH
from urllib import request
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth.models import User as U
from record.models import Prison
from django.contrib.auth.decorators import login_required
from django.db import transaction 
 
 
from email.headerregistry import Address
from multiprocessing import context 
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from.models import * 
from.forms import *
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from . models import *
from account.forms import *
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from account.decorators import *

 
class UsersForm(UserCreationForm):
     
        class Meta:
            model=User
            fields=['username','password1', 'password2','email','first_name','last_name','phone','address','prison','is_SuperManager','is_Admin','is_Manager','is_DataEncoder']

    # firstname = forms.CharField(max_length=30,widget=forms.TextInput(),label="Firstname")
    # lastname = forms.CharField(max_length=30, widget=forms.TextInput(), label="Lastname")
    # phone = forms.CharField(max_length=30, widget=forms.TextInput(),label='Mobile No') 
    # email = forms.CharField(max_length=30, widget=forms.TextInput(), label="Email")
    # address = forms.CharField(max_length=30,widget=forms.TextInput(),label="Address")  
    # admin = forms.BooleanField( label="Admin" ,required=False )
    # manager = forms.BooleanField( label="Manager", required=False)
    # encoder = forms.BooleanField( label="DataEncoder", required=False)

    # class Meta(UserCreationForm.Meta):
    #     model = User 
 
        

    # @transaction.atomic()
    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.is_Admin =  self.cleaned_data.get('admin')
    #     user.is_Manager =  self.cleaned_data.get('manager')
    #     user.is_DataEncoder =  self.cleaned_data.get('encoder')
    #     user.first_name = self.cleaned_data.get('firstname')
    #     user.address= self.cleaned_data.get('address')
    #     user.last_name = self.cleaned_data.get('lastname') 
    #     user.phone = self.cleaned_data.get('phone')
    #     user.email = self.cleaned_data.get('email') 
    #     user.save()