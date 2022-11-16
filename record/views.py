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



 
# Create your views here. 

def home(request):
    return render(request,'index.html')

@login_required
@superuser_required()
def UserRegister(request):
    form = UsersForm()
    if request.method == "POST":
        form =  UsersForm(request.POST or None)
        if form.is_valid():  
               form.save()
               return redirect('user_list') 
            
    
    
    return render(request,'registration.html',{'form':form})


@login_required
@Admin_required()
def adminUserRegister(request):
    form =  UsersForm()
    if request.method == "POST":
        form = UsersForm(request.POST or None)
        if form.is_valid():  
            f=form.save(commit=False)
            f.prison=request.user.prison
            f.save()
            return redirect('user_list')
            
    return render(request,'registration.html',{'form':form})
@login_required
@superuser_required
def edit_user(request, User_id):
    ur = User.objects.get(id=User_id)
    forms = UsersForm(instance=ur)
    if request.method == 'POST':
        forms = UsersForm(request.POST, instance=ur)
        if forms.is_valid(): 
            forms.save()
            return redirect('user_list')
    context = {
        'form': forms
    }
    return render(request, 'registration.html', context) 
@login_required
@Admin_required 
def admin_edit_user(request, User_id):
    ur = User.objects.get(id=User_id)
    forms = UsersForm(instance=ur)
    if request.method == 'POST':
        forms = UsersForm(request.POST, instance=ur)
        if forms.is_valid():  
            f=forms.save(commit=False)
            f.prison=request.user.prison
            f.save()
            return redirect('user_list')
    context = {
        'form': forms
    }
    return render(request, 'registration.html', context)
 
def SignInView(request): 

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password'] 
        user = auth.authenticate(username=username, password=password)
        if user is not None: 
            # if user.is_active:
                auth.login(request,user)
                return redirect('index')
        else:
            messages.error(request,"You have Entered invalid Username/Password.")
    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
@AS_required()
def User_list(request):
    if request.user.is_Admin:
      us = User.objects.filter(prison=request.user.prison) 

    elif request.user.is_SuperManager:
         us=User.objects.filter(is_Admin = 1 )  
    
    else :
        us=User.objects.filter(is_Admin = 1 )  | User.objects.filter(is_SuperManager=1)
    
    context = {
        'User': us
    }
    return render(request, 'users/users.html', context)

@login_required
@SuperManager_required()
def Users(request,Prison_id):
    us = User.objects.filter(prison=Prison_id)
    context = {
        'User': us
    }
    return render(request, 'users/users.html', context)

@login_required
@AS_required()
def deactivate_user(request, User_id):
    record = User.objects.get(id=User_id)
    record.is_active=False
    record.save()
    return redirect('user_list')
 
@login_required
@AS_required()
def activate_user(request, User_id):
    record = User.objects.get(id=User_id)
    record.is_active=True
    record.save()
    return redirect('user_list')
 
 
def home(request):
    return render(request,'home.html')  
  
@login_required
def index(request):
    return render(request,'index.html')  
  
   
@login_required
def  region(request):
    if request.method=='POST':
        name=request.POST['cname'] 
        CentralPrison( Name=name ).save()
    return render(request,'Region.html')


#Crime

# @login_required 
# @DataEncoder_required()
# def  crime(request):
#     forms=CrimeForm()
#     if request.method=='POST': 
#         forms=CrimeForm(request.POST)
#         if forms.is_valid(): 
#             f=forms.save(commit=False)
#             f.createdby=request.user
#             f.save()
#             return redirect('crime_list')
#     context = {
#         'form': forms
#     }
        
         
#     return render(request,'crime/crime.html',context)

# @login_required
# @MAD_required()
# def crime_list(request):
#     crime = Crime.objects.all()
#     context = {
#         'crime': crime
#     }
#     return render(request, 'crime/crime_list.html', context)

# @login_required
# @DataEncoder_required()
# def edit_crime(request, Crime_id):
#     pr = Crime.objects.get(id=Crime_id)
#     forms = CrimeForm(instance=pr)
#     if request.method == 'POST':
#         forms = CrimeForm(request.POST, instance=pr)
#         if forms.is_valid():
#             f=forms.save(commit=False)
#             f.createdby=request.user
#             f.save()
#             return redirect('crime_list')
#     context = {
#         'form': forms
#     }
#     return render(request, 'crime/edit_crime.html', context)
 
 
#prison Views
 
@login_required
@superuser_required()
def prison(request):
    forms = PrisonForm()
    if request.method == 'POST':
        forms = PrisonForm(request.POST)
        if forms.is_valid(): 
            forms.save()
            return redirect('register')
    context = {
        'form': forms
    }
    return render(request, 'prison/prison.html', context)
 
@login_required
@Super_required()
def prison_list(request):
    prison = Prison.objects.all()
    context = {
        'pri': prison
    }
    return render(request, 'prison/prison_list.html', context)
@login_required
@superuser_required()
def edit_prison(request, Prison_id):
    pr = Prison.objects.get(id=Prison_id)
    forms = PrisonForm(instance=pr)
    if request.method == 'POST':
        forms = PrisonForm(request.POST, instance=pr)
        if forms.is_valid():
            f=forms.save(commit=False)
            f.createdby=request.user
            f.save()
            return redirect('prison_list')
    context = {
        'form': forms
    }
    return render(request, 'prison/edit_prison.html', context)
 
 
 
@login_required
@DataEncoder_required()
def criminal(request):
    forms = CriminalForm()
    if request.method == 'POST':
        forms = CriminalForm(request.POST)
        if forms.is_valid (): 
            f=forms.save(commit=False)
            f.createdby=request.user
            f.prison=request.user.prison
            f.save()
            return redirect('criminal_list')
    context = {
        'form': forms
    }
    return render(request, 'criminal/criminal.html', context) 
 
@login_required
@MAD_required()
def criminal_list(request):
    crs = Criminal.objects.filter(Status=True,prison=request.user.prison)
    context = {
        'F': crs, 
            }
    
    
    return render(request, 'criminal/criminal_list.html', context)

@login_required
@SuperManager_required()
def criminals(request,Prison_id):
    crs = Criminal.objects.filter(prison=Prison_id)
    context = {
        'F': crs
    }
    return render(request, 'criminal/criminal_list.html', context)


@login_required
@Manager_required()
def ReleasedCriminal_list(request):
    crs = Criminal.objects.filter( Status=False,prison=request.user.prison)
    context = {
        'F': crs
    }
    return render(request, 'criminal/releasedCriminal.html', context)

@login_required
@MAD_required()
def CriminalDetial(request ,Criminal_id):
    crs=Criminal.objects.get(id=Criminal_id) 
    
    context = {
        'criminal': crs
    }
    return render(request, 'criminal/CriminalDetial.html', context)
 
@login_required
@DataEncoder_required()
def edit_criminal(request, Criminal_id):
    cri = Criminal.objects.get(id=Criminal_id)
    forms = CriminalForm(instance=cri)
    if request.method == 'POST':
        forms = CriminalForm(request.POST, instance=cri)
        if forms.is_valid():
            f=forms.save(commit=False)
            f.createdby=request.user
            f.prison=request.user.prison
            f.save()
            return redirect('criminal_list')
    context = {
        'form': forms
    }
    return render(request, 'criminal/edit_criminal.html', context)
   
@login_required
@Manager_required()
def releaseCriminal(request, Criminal_id):
    record = Criminal.objects.get(id=Criminal_id)
    record.Status=False
    record.save()
    return redirect('criminal_list')
 
#visitors
 
@login_required
@DataEncoder_required()
def visitor(request):
    forms = VisitorForm()
    if request.method == 'POST':
        forms = VisitorForm(request.POST)
        if forms.is_valid():
            f=forms.save(commit=False)
            f.createdby=request.user
            f.prison=request.user.prison
            f.save()
            return redirect('visitor_list')
    context = {
        'form': forms
    }
    return render(request, 'visitor/visitor.html', context)
 
@login_required
@MAD_required()
def visitor_list(request):
    visitor = Visitor.objects.filter(prison=request.user.prison)
    context = {
        'visit': visitor
    }
    return render(request, 'visitor/visitor_list.html', context)

@login_required
@SuperManager_required()
def visitors(request,Prison_id):
    visitor = Visitor.objects.filter(prison=Prison_id)
    context = {
        'visit': visitor
    }
    return render(request, 'visitor/visitor_list.html', context)
 
@login_required
@DataEncoder_required()
def edit_visitor(request, visitor_id):
    vr = Visitor.objects.get(id=visitor_id)
    forms = VisitorForm(instance=vr)
    if request.method == 'POST':
        forms = VisitorForm(request.POST, instance=vr)
        if forms.is_valid():
            f=forms.save(commit=False)
            f.createdby=request.user
            f.save()
            return redirect('visitor_list')
    context = {
        'form': forms
    }
    return render(request, 'visitor/edit_visitor.html', context)
 