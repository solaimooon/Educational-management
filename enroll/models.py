from django.db import models
from django_jalali.db import models as jmodels
from django.contrib.auth.models import User


class klass(models.Model):
    name=models.CharField(max_length=150)
    teacher=models.ForeignKey(User,on_delete=models.SET_NULL,related_name='have_teacher',null=True)
    course=models.PositiveIntegerField()
    start_date=jmodels.jDateField()
    end_data=jmodels.jDateField()
    start_time=models.TimeField(null=True)
    end_time=models.TimeField(null=True)
    student=models.ManyToManyField(User,related_name='have_staudent')
    status=models.BooleanField(null=True)












# Create your models here.
