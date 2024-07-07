from django.urls import path
from .views import *

app_name='athentication'

urlpatterns = [
path('', login_form, name='log in'),
path('sign_up/', sign_up_form, name='sign up'),
path('reset_password/',reset_password_form,name='reset_password')
]