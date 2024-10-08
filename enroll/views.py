from django.shortcuts import render

from django.shortcuts import redirect
from .forms import *
from .models import *
from score.models import *
from django.shortcuts import get_object_or_404

def enroll_choose(request):
    return render(request,'enroll/choose_enroll_or_edit.html')


def create_class_view(request):
    if request.method=='GET':
        # creat the pure form of kalss info and enroll student
        kalss_form_object=klass_form()
        student_picker_object=enroll_student_form()
        return render(request,"enroll/create_class.html",{"klass_form_object":kalss_form_object,"student_picker_object":student_picker_object})
        # save form
    else:
        kalss_form_object = klass_form(request.POST)
        if kalss_form_object.is_valid():
            klass_object=kalss_form_object.save()
            students = request.POST.getlist('students')
            print(":دانش اموزان", students)
            klass_object.student.set(students)
            return redirect("https://toplearn.com/")


#show class for teather in own dashbord
def my_class_oprator_view(request):
    klass_object=klass.objects.filter(teacher=request.user.id).order_by('-course')
    return render(request,'enroll/my_class.html',{"klass_object":klass_object})


#show class for student in own dashbord
def my_class_student_view(request):
    enroll_objects=link_table.objects.filter(student_id=request.user.id)
    return render(request,'enroll/my_class_student.html',{"enroll_objects":enroll_objects})

# report generaly to studnet
def report_general_student_view(request,id_enroll):
    # sum of emtiyazat
    sum_emtiyaz_for_all_session=get_object_or_404(SUM_final,enroll=id_enroll)
    # colculate the rank
    all_object_of_sum=SUM_final.objects.all().order_by('SUM')
    counter=1
    for object in all_object_of_sum:
        if object==sum_emtiyaz_for_all_session:
            break
        else:
            counter+=1
    #end calculate
    return render(request,'enroll/report.html',{"sum_emtiyaz_for_all_session":sum_emtiyaz_for_all_session,"rank":counter})

# report point student
def report_point_detail_view(request):
    pass






