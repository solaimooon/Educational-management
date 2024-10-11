from django.forms import ModelForm, Textarea
from django import forms
from athentication.models import *
from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget
from django.core.exceptions import ValidationError


class update_extra_user_data(ModelForm):
    class Meta:
        model = extra_user_data
        fields = ['age', 'adress', 'meli_cood', 'sex', 'image']
        widgets = {
            'adress': Textarea(attrs={'cols': 80, 'rows': 3}),
            'sex': forms.RadioSelect(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super(update_extra_user_data, self).__init__(*args, **kwargs)
        self.fields['age'] = JalaliDateField(label=('تاریخ تولد'), widget=AdminJalaliDateWidget)

    def clean_image(self):
        image = self.cleaned_data.get('image')

        if image:
            # بررسی اینکه image یک فایل معتبر است
            if hasattr(image, 'size'):
                # محدودیت حجم فایل به 100 کیلوبایت
                if image.size > 100 * 1024:
                    raise ValidationError("حجم تصویر نمی‌تواند بیشتر از 100 کیلوبایت باشد.")
            else:
                return image




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
                'placeholder': 'example@gmail.com',
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
