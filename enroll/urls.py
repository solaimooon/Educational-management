from django.urls import path
from .views import *
app_name='enroll'
urlpatterns = [
    path('',enroll_choose, name='enroll_choose'),
    path("create_class/",create_class_view,name='create_class'),
    path("my_class/",my_class_view,name='my_class')


]