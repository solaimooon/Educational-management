from django.forms import ModelForm
from .models import *

class Sign_up_form(ModelForm):
    class Meta:
        model = User
        fields=['username','password']