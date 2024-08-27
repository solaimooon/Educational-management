from django.urls import path
from .views import *
app_name='score'
urlpatterns = [
    path('',choose_date, name='choose_date'),

]