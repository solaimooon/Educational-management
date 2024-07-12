from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth.models import User

def dashbord(request):
    # render oprator page if usre be staff
    if request.user.is_staff==True:
        return render(request, 'dashbord_opratoe/oprator_base.html')
    # render student base page if usre not be staff
    else:
        return redirect("https://www.w3schools.com/python/gloss_python_string_length.asp")
# Create your views here.
