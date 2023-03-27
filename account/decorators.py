from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

def superuser_required(function=None, redirect_field_name = REDIRECT_FIELD_NAME, login_url = 'login'):
    
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_superuser,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator 
def Super_required (function=None, redirect_field_name = REDIRECT_FIELD_NAME, login_url = 'login'):
    
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_superuser or u.is_SuperManager,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
def Admin_required(function=None, redirect_field_name = REDIRECT_FIELD_NAME, login_url = 'login'):
     
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_Admin,
        login_url = login_url,
        redirect_field_name= redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def AS_required(function=None, redirect_field_name = REDIRECT_FIELD_NAME, login_url = 'login'):
    
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_Admin or u.is_superuser or u.is_SuperManager,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
def Manager_required(function=None, redirect_field_name = REDIRECT_FIELD_NAME, login_url = 'login'):
    
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_Manager ,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
def DataEncoder_required(function=None, redirect_field_name = REDIRECT_FIELD_NAME, login_url = 'login'):
    
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_DataEncoder,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def MAD_required(function=None, redirect_field_name = REDIRECT_FIELD_NAME, login_url = 'login'):
    
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_Manager or u.is_Admin or u.is_DataEncoder or u.is_SuperManager ,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
    
def SuperManager_required(function=None, redirect_field_name = REDIRECT_FIELD_NAME, login_url = 'login'):
    
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_SuperManager ,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator