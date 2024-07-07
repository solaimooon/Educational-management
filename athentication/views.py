from django.shortcuts import render

def login_form(request):
    return render(request,'sign up _ log in/page-login-simple.html')


def sign_up_form(request):
    return render(request,'sign up _ log in/page-signup-simple.html')

def reset_password_form(request):
    return render(request,'sign up _ log in/page-reset-password-simple.html')
# Create your views here.
