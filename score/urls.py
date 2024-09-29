from django.urls import path
from .views import *
app_name='score'
urlpatterns = [
    path('<int:id>/',choose_date_view, name='choose_date'),
    path('post_score/',post_score_view,name='post_score')

]