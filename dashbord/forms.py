from django.forms import ModelForm
from django import forms
from athentication.models import *

class update_extra_user_data(ModelForm):
    class Meta:
        model=extra_user_data
        fields=['age','adress','father_name','type','meli_cood','sex','image']


class update_user_data(ModelForm):
    class Meta:
        model = User
        fields=['first_name','last_name','email']


