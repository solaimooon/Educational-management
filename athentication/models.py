from django.db import models
from django.contrib.auth.models import User

sex = (
    ('زن','زن'),
    ('مرد', 'مرد'),)


type = (
    ('اوپراتور','operator '),
    ('معلم','teacher '),
    ('student','دانش اموز'),
    ('free student',"مستمع ازاد")
)


class extra_user_data(models.Model):
    age=models.IntegerField(null=True,blank=True,verbose_name='سن')
    adress=models.CharField(null=True,blank=True,max_length=500,verbose_name='ادرس')
    father_name=models.CharField(null=True,blank=True,max_length=50,verbose_name='نام پدر ')
    #type of user for ristricing
    type =models.CharField(null=True,blank=True,max_length=50, choices=type)
    meli_cood = models.CharField(null=True,blank=True,max_length=50, verbose_name="کد ملی")
    sex = models.CharField(null=True,blank=True,max_length=50, choices=sex)
    forign_key = models.ForeignKey(User, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='personality_picture/',default="personality_picture/boy.png")
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
