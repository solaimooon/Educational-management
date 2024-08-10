from django.db import models
from django.contrib.auth.models import User


type = (
    ('operator','اوپراتور'),
    ('teacher','معلم'),
    ('student','دانش اموز'),
    ('Guest',"مهمان")
)


class extra_user_data(models.Model):
    sex_choice = (
        ('male', 'مرد'),
        ('female', 'زن')
    )
    age=models.DateField(verbose_name='سن')
    adress=models.CharField(max_length=500,verbose_name='ادرس')
    #type of user for ristricing
    type =models.CharField(max_length=50, choices=type,default="Guest")
    meli_cood = models.CharField(null=True,blank=True,max_length=50, verbose_name="کد ملی")
    sex = models.CharField(null=True,blank=True,max_length=50, choices=sex_choice,default='male')
    forign_key = models.ForeignKey(User, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='personality_picture/',default="personality_picture/boy.png")


class phone(models.Model):
    phone_owner = (
        ('itself', 'شخصی'),
        ('father', 'پدر'),
        ('mather', 'مادر'),
    )
    phone_number=models.CharField(max_length=50,blank=True,verbose_name='شماره تلفن ')
    owner = models.CharField(max_length=6, choices=phone_owner,blank=True, verbose_name='مالکیت')
    forign_key = models.ForeignKey(User, on_delete=models.CASCADE,)

# Create your models here.
