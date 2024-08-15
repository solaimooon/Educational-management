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
    student=models.ManyToManyField(User,related_name='have_staudent',through='link_table')
    status=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True)


class link_table(models.Model):
    klass_id = models.ForeignKey(klass,on_delete=models.CASCADE)
    student_id = models.ForeignKey(User,on_delete=models.CASCADE)
    result_of_class = models.BooleanField()












# Create your models here.
