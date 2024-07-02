from django.db import models
from django.contrib.auth.models import User

sex = (
    ('زن','زن'),
    ('مرد', 'مرد'),)


type = (
    ('اوپراتور','operator '),
    ('معلم','teacher '),
    ('student','دانش اموز')
)


class extra_user_data(models.Model):
    age=models.IntegerField(verbose_name='سن')
    adress=models.CharField(max_length=255,verbose_name='ادرس')
    father_name=models.CharField(max_length=50,verbose_name='نام پدر ')
    #type of user for ristricing
    type =models.CharField(max_length=50, choices=type)
    meli_cood = models.CharField(max_length=50, verbose_name="کد ملی")
    sex = models.CharField(max_length=50, choices=sex)
    forign_key = models.ForeignKey(User, on_delete=models.CASCADE)
phone_owner = (
    ('itself','شخصی'),
    ('father', 'پدر'),
    ('mather','مادر'),
)
class phone(models.Model):
    phone_number=models.CharField(max_length=50,blank=True,verbose_name='شماره تلفن ')
    owner = models.CharField(max_length=6, choices=phone_owner, verbose_name='مالکیت')
    exta_user_data = models.ForeignKey(User, on_delete=models.CASCADE,)

# Create your models here.
