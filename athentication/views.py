import random
import requests
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import *
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

def login_form(request):
    if request.method=='GET':
        return render(request,'sign up _ log in/page-login-simple.html')
    else:
        sign_in_form=sign_in(request.POST)
        # validate the data post from the form html
        if sign_in_form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            # check the user exist or not
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/dashbord/')



def sign_up_form(request):
    if request.method == 'GET':
        return render(request,'sign up _ log in/page-signup-simple.html')
    elif request.method == 'POST':
        # create the python form object by data recive from post request
        sign_up_form=Sign_up_form(request.POST)
        if sign_up_form.is_valid():
            # if the form valid , get username,passwoerd and redirect to verification view
            global username
            username=sign_up_form.cleaned_data["username"]
            global password
            password=sign_up_form.cleaned_data["password"]
            # validate amount of password charector
            str_password=str(password)
            amount_charctor=len(str_password)
            if amount_charctor<8 or amount_charctor==8:
                messages.add_message(request, messages.ERROR, "حداقل طول رمز عبور 8 کاراکتر میباشد")
                return redirect('/athentication/sign_up/')
            return HttpResponseRedirect(reverse("athentication:verification"))

        else:
            # IF the user exist return this massage
            messages.add_message(request, messages.ERROR, "نام کاربری تکراری میباشد")
            return redirect('/athentication/sign_up/')



def reset_password_form(request):
    return render(request,'sign up _ log in/page-reset-password-simple.html')
# Create your views here.


# this function send verification and render the verification template
def verification (request):

    if request.method=='GET':
        # create the random codde between 1001 until 9999 and define it global to use all over the fanction
        global verification_code
        # creat the random number between the range give it
        verification_code = random.randint(1001, 9999)
        print(verification_code)
        key = '4338526C6C676E4C6932475636665246734C336E6F53666D735643652F3836627850537A426F796E674A4D3D'
        # this is the api of cavenegar , pass the key to url
        api = 'https://api.kavenegar.com/v1/%s/verify/lookup.json' % key
        # data must be send to api
        paloyd = {'receptor': str(username), 'token': str(verification_code), "template": "verify"}
        # request to kavenegar to send massage
        #response = requests.post(api, data=paloyd)
        return render(request,'sign up _ log in/verification.html')
    elif request.method=='POST':
        # get the numbers
        number1 = request.POST.get('number1')
        number2 = request.POST.get('number2')
        number3 = request.POST.get('number3')
        number4 = request.POST.get('number4')
        #concat the numbers together
        number=int (number1+number2+number3+number4)
        # validate the user insert the cerect valodation code
        if number == verification_code:
            user = User.objects.create_user(username=username,password=password)
            return redirect('/dashbord/')


