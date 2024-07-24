from django.forms import ModelForm
from django import forms
from athentication.models import *
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime

class update_extra_user_data(ModelForm):
    class Meta:
        model=extra_user_data
        fields=['age','adress','father_name','type','meli_cood','sex','image']
    def __init__(self, *args, **kwargs):
        super(update_extra_user_data, self).__init__(*args, **kwargs)
        self.fields['age'] = JalaliDateField(label=('تاریخ تولد'), # date format is  "yyyy-mm-dd"
            widget=AdminJalaliDateWidget # optional, to use default datepicker
        )



class update_user_data(ModelForm):
    class Meta:
        model = User
        fields=['first_name','last_name','email']


