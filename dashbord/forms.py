from django.forms import ModelForm, Textarea
from django import forms
from athentication.models import *
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime


class update_extra_user_data(ModelForm):
    class Meta:
        model = extra_user_data
        fields = ['age', 'adress', 'meli_cood', 'sex', 'image']
        widgets = {
            'adress': Textarea(attrs={'cols': 80, 'rows': 3}),
            'sex': forms.RadioSelect(attrs={'class': 'form-check-input'})}

    # override the init function of calss model form for date picker

    def __init__(self, *args, **kwargs):
        super(update_extra_user_data, self).__init__(*args, **kwargs)
        self.fields['age'] = JalaliDateField(label=('تاریخ تولد'),  # date format is  "yyyy-mm-dd"
                                             widget=AdminJalaliDateWidget  # optional, to use default datepicker
                                             )


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'firstNameLabel',
                'placeholder': 'محمد',
                'aria-label': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'lastNameLabel',
                'placeholder': 'محمدی',
                'aria-label': 'Last Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'id': "emailLabel",
                'placeholder': 'example@gmial.com',
            })

        }


class phone_form(forms.ModelForm):
    class Meta:
        model = phone
        fields = ['phone_number', 'owner']
        widgets = {
            'phone': forms.TextInput(attrs={
                'class': 'js-input-mask form-control',
                'id': 'phoneLabel',
                'placeholder': '+x(xxx)xxx-xx-xx',
                'aria-label': '+x(xxx)xxx-xx-xx',
                'value': '+1(605)5618929',
                'data-hs-mask-options': '{"mask": "+{0}(000)000-00-00"}'
            }),
            'additional_phone_select': forms.Select(attrs={
                'class': 'js-select form-select tomselected ts-hidden-accessible',
                'data-hs-tom-select-options': '{"width": "8rem", "hideSearch": true}',
                'id': 'tomselect-1',
                'tabindex': '-1'
            })
        }
