from django.forms import ModelForm, Textarea
from django import forms
from enroll.models import *
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime



class klass_form(forms.ModelForm):
        class Meta:
            model = klass
            fields = ['name', 'teacher', 'course', 'start_date', 'end_data', 'start_time', 'end_time', 'student',
                      'status']
            widgets = {
            'start_time':forms.TimeInput(attrs={
            'type': 'time',  # HTML5 time input type
            'id': 'appt',  # id attribute for the time field
            }),
            'end_time': forms.TimeInput(attrs={
                'type': 'time',  # HTML5 time input type
                'id': 'appt',  # id attribute for the time field

            })
            }




        # override the init function of calss model form for date picker
        def __init__(self, *args, **kwargs):
            super(klass_form, self).__init__(*args, **kwargs)
            self.fields['start_date'] = JalaliDateField(label=('تاریخ شورع کلاس'),  # date format is  "yyyy-mm-dd"
                                                widget=AdminJalaliDateWidget)  # optional, to use default datepicker
            self.fields['end_data'] = JalaliDateField(label=('تاریخ پایان کلاس'),  # date format is  "yyyy-mm-dd"
                                                 widget=AdminJalaliDateWidget)  # optional, to use default datepicker
