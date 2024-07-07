from django.urls import path
from .views import *

app_name='athentication'

urlpatterns = [
path('', login_form, name='log in'),
path('sign_up/', sign_up_form, name='sign up')
]