from django.shortcuts import render
from datetime import datetime
from datetime import timedelta
from enroll.models import *


def choose_date(request,id):
    # get the class object
    class_object=klass.objects.filter(id=id)[0]
    start_date=str(class_object.start_date)
    end_data=str(class_object.end_data)
    # create the datetime object
    date=datetime.strptime(start_date, "%Y-%m-%d")
    end_data=datetime.strptime(end_data, "%Y-%m-%d")
    list_date=[]
    while date<=end_data:
        # append the time to list and slice datetiem object form time
        list_date.append(str(date)[0:11])
        date=date + timedelta(days=7)
    return render(request,'score/choose_date.html',{"dates":list_date})

# Create your views here.
