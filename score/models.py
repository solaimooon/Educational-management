from django.db import models
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels
from enroll.models import *


class presence_absence(models.Model):
    enroll=models.ForeignKey(link_table,on_delete=models.CASCADE)
    time=models.TimeField()
    was=models.BooleanField()
    date=jmodels.jDateField(null=True)


class score (models.Model):
    method=(
        ('kosha_ravankhani','kosha_ravankhani'),
        ('kosha_tajvid','kosha_tajvid'),
        ('noramal','noramal')
    )
    enroll=models.ForeignKey(link_table,on_delete=models.CASCADE)
    date_for=jmodels.jDateField()
    creat_at=models.DateField(auto_now_add=True,null=True)
    method=models.CharField(choices=method,max_length=50)
    ons=models.PositiveIntegerField(null=True)


class type(models.Model):
    name=models.CharField(max_length=50)
    avalable=models.IntegerField()

    def __str__(self):
        return self.name


class amount(models.Model):
    score=models.ForeignKey(score,on_delete=models.CASCADE)
    number=models.IntegerField()
    type=models.ForeignKey(type,on_delete=models.SET_NULL,null=True)


# define views sum_final and each session.
class sum_emtiyazat(models.Model):
    id = models.BigIntegerField(primary_key=True)
    score=models.ForeignKey(score,on_delete=models.DO_NOTHING)
    enroll=models.ForeignKey(link_table,on_delete=models.DO_NOTHING)
    date_for=jmodels.jDateField()
    sumed_emtiyaz=models.DecimalField(max_digits=10,decimal_places=2)
    class Meta:
        managed = False
        db_table = 'sum_emtiyazat'



