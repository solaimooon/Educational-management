from django.shortcuts import render
from datetime import datetime
from datetime import timedelta
from enroll.models import *
from .forms import *
from .models import *
import urllib
from django.http import HttpResponseRedirect
from django.urls import reverse
import jdatetime
# massage framwork
from django.contrib import messages
from django.shortcuts import redirect

def choose_date_view(request,id):
    # get the klass_id and save to session
    request.session["klass_id"]=request.GET.get("klass_id")
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
    # create sessoin "enroll"
    request.session["enroll"] = "هنوز حضوری ثبت نکرده اید"
    return render(request,'score/choose_date.html',{"dates":list_date})

# save the hozore and score
def post_score_view(request,id=None):
    # (GET method)show the form
    if request.method == 'GET':
        # get the date whene clik date
        date_temp = request.GET.get('date')
        if date_temp!=None:
            global date
            date=date_temp
        try:
            # convert sting date to jdate object
            date=date.split("-")
            date=jdatetime.date(int(date[0]),int(date[1]),int(date[2]))
        finally:
            # creat presence_absence object with apropriate enroll choose
            # show the class.student(enroll) to choose
            presence_absence_form_object=presence_absence_form(klass_id=request.session["klass_id"])
            # get the class object
            klass_object=klass.objects.filter(pk=request.session["klass_id"])[0]
            # creat pure emtiyaz form
            pure_emtiyaz_and_form_object = pure_emtiyaz_and_ons_form(klass_id=request.session["klass_id"])
            # show the basic_kosha_form
            if klass_object.level.name in ["روانخوانی متوسط","روانخوانی پایه","روانخوانی خوب"]:
                # get emtiyazat that saved before
                # call the retrive_score_saved
                list_of_scores = retrive_score_saved(request, date)
                print(list_of_scores)
                # get absent or present saved before
                # call retirve present function
                presents_objects=retrive_present_or_absent(request)
                basic_kosha_form_object=basic_kosha_form()
                return render(request,'score/basic_form_score.html',{"basic_kosha_form_object":basic_kosha_form_object,"presence_absence_form_object":presence_absence_form_object,"pure_emtiyaz_and_form_object":pure_emtiyaz_and_form_object,"list_of_scores":list_of_scores,"presents_objects":presents_objects})
    # (POST method) creat new present and score object
    elif request.method == "POST":
        # creat presence object if "was" field in post request
        if "was_or_not_or" in request.POST:
            presence_absence_form_object = presence_absence_form(request.POST)
            # validation
            if presence_absence_form_object.is_valid():
                presence_absence.objects.create(
                    date=date,
                    time=presence_absence_form_object.cleaned_data['time'],
                    was_or_not_or=presence_absence_form_object.cleaned_data['was_or_not_or'],
                    enroll=presence_absence_form_object.cleaned_data['enroll']
                )
                request.session["enroll"]=presence_absence_form_object.cleaned_data['enroll'].id

                return HttpResponseRedirect(reverse("score:post_score"))
            else:
                print(presence_absence_form_object.errors.as_data)
        # creat score object
        else:
            # save score object
            new_score_pure_object=score.objects.create(enroll=link_table.objects.get(pk=request.POST.get('enroll')),method='kosha_ravankhani',ons=request.POST.get('ons'),date_for=date)
            basic_kosha_form_object=basic_kosha_form(request.POST)
            if basic_kosha_form_object.is_bound:
                if basic_kosha_form_object.is_valid():
                    print (basic_kosha_form_object.data.dict())
                    for name_field,amount_temp in basic_kosha_form_object.cleaned_data.items():
                        if amount_temp==None:
                            continue
                        new_score_amount_object=amount()
                        new_score_amount_object.score=new_score_pure_object
                        new_score_amount_object.number=amount_temp
                        new_score_amount_object.type=type.objects.filter(name=name_field)[0]
                        print ("number",new_score_amount_object.number)
                        print("type",new_score_amount_object.type)
                        new_score_amount_object.save()
                    return HttpResponseRedirect(reverse("score:post_score"))
# delete the scores
def delete_csore_view(request,id):
    if request.method == 'POST':
        print("delete:",id)
        score.objects.filter(id=id).delete()
        return HttpResponseRedirect(reverse("score:post_score"))


# delete present object
def delete_present_view(request,id):
    if request.method == 'POST':
        print("delete:",id)
        presence_absence.objects.filter(id=id).delete()
        return HttpResponseRedirect(reverse("score:post_score"))




# function , not view
def retrive_score_saved(request,date):
    enrolls = link_table.objects.filter(klass_id=request.session.get("klass_id"))
    scores = score.objects.filter(enroll_id__in=enrolls, date_for=date)
    amounts = amount.objects.filter(score_id__in=scores).order_by("score_id")

    print("amounts", amounts)

    # Initialize lists
    second_list = []
    first_list = []

    # Loop through amounts
    for idx, amont in enumerate(amounts):
        if idx == 0:  # For the first record
            first_list.append(amont)
            current_score_id = amont.score_id
        else:
            if amont.score_id == current_score_id:  # Same score_id
                first_list.append(amont)
            else:  # Different score_id, add the current list to second_list
                second_list.append(first_list)
                first_list = [amont]  # Reset first_list with the new amount
                current_score_id = amont.score_id
    # Don't forget to add the last grouped amounts
    if first_list:
        second_list.append(first_list)
    return second_list


def retrive_present_or_absent(request):
    enrolls = link_table.objects.filter(klass_id=request.session.get("klass_id"))
    present_object=presence_absence.objects.filter(enroll__in=enrolls,date=date)
    return present_object








