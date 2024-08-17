from django.shortcuts import render
from .forms import *

def enroll_choose(request):
    return render(request,'enroll/choose_enroll_or_edit.html')


def create_class_view(request):
    kalss_form_object=klass_form()
    student_picker_object=ColorForm()
    print(student_picker_object)
    return render(request,"enroll/create_class.html",{"klass_form_object":kalss_form_object,"student_picker_object":student_picker_object})


