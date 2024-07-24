from athentication.models import *
from .forms import *
from django.contrib.auth.models import User

from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse


@login_required(login_url='/athentication/')
def dashbord(request):
    # render oprator page if usre be staff
    if request.user.is_staff==True:
        extra_data=extra_user_data.objects.filter(forign_key=request.user.pk)[0]
        # keep the picture of user in session_for save the adress of picture we must save the url
        request.session["picture"] =extra_data.image.url
        return render(request, 'dashbord_opratoe/oprator_index.html',{"extra_data":extra_data})
    # render student base page if usre not be staff
    else:
        # beacuse of sign up and the new user dont have any record in extra_user_data we need try/exeption
        try:
            extra_data = extra_user_data.objects.filter(forign_key=request.user.pk)[0]
            request.session["picture"] = extra_data.image.url
            return render(request, 'dashbord_student/student_index.html', {"extra_data": extra_data})
        except:
            #we need set picture in approch below beacuse we donat have record in extra_user_data
            request.session["picture"] = '/media/personality_picture/boy.png'
            return render(request, 'dashbord_student/student_index.html')

# Create your views here.


@login_required(login_url='/athentication/')
def student_info_list(request):
    students=User.objects.filter(is_staff=False)
    students_extra_data=extra_user_data.objects.raw(
            "select * from athentication_extra_user_data where forign_key_id in(select id from auth_USER where is_staff=False)")
    # integrate the element of first itrable to element of second iterable as tuple -first element of first list to first element of second list
    zip_student=list(zip(students, students_extra_data))
    print(list(zip_student))
    contex={"zip_student":zip_student}

    return render(request, 'dashbord_opratoe/oprator_student_list.html', contex)

@login_required(login_url='/athentication/')
def profile(request,pk=None):
    #the staff profile
    if request.user.is_staff == True:
        student = User.objects.filter(id=pk)[0]
        student_extra_data = extra_user_data.objects.filter(forign_key=pk)[0]
        return render(request,'dashbord_opratoe/operator_profile.html',{"user_data":student,"extra_user_data":student_extra_data})
    # the student profile
    else:
        # show profile
        if request.method=='GET':
            student = User.objects.filter(id=pk)[0]
            student_extra_data = extra_user_data.objects.filter(forign_key=pk)[0]
            image_form=update_extra_user_data()
            return render(request, 'dashbord_student/student_profile.html',{"user_data": student, "extra_user_data": student_extra_data,'form':image_form})
        # update profile
        else:
            # find the pk of user in extra_user_data tabel if there isnt we undrestand by ty/exeptin and create new record for it
            # for crete form with file data we must add request.files
            extra_user_data_form=update_extra_user_data(request.POST,request.FILES)
            # handel update or complite profile by try/exeption
            try:
                # update data
                extra_user_object = extra_user_data.objects.filter(forign_key=request.user.pk)[0]
                if extra_user_data_form.is_valid():
                    extra_user_object.image=extra_user_data_form.cleaned_data["image"]
                    extra_user_object.age = extra_user_data_form.cleaned_data["age"]
                    extra_user_object.save()
                    # update the url of picture in session
                    request.session["picture"]=extra_user_object.image.url
                    return HttpResponseRedirect(reverse("dashbord:profile",kwargs={'pk':request.user.id}))
            except:
                # create new record
                if extra_user_data_form.is_valid():
                    extra_user_data_object=extra_user_data()
                    extra_user_data_object.image=extra_user_data_form.cleaned_data["image"]
                    extra_user_data_object.forign_key=request.user
                    extra_user_data_object.save()
                    request.session["picture"] = extra_user_data_object.image.url
                    return HttpResponseRedirect(reverse("dashbord:profile",kwargs={'pk':request.user.id}))








