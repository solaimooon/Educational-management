from django.shortcuts import render

from django.shortcuts import redirect
from .forms import *
from .models import *

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
    return render(request,'enroll/my_class_student.html')





