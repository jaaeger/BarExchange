from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

from Comments.forms import UserRegisterForm, UserLoginForm
from .models import Bars

# Create your views here.
def index(request):
    bars = Bars.objects.all()
    context = {
        'bars': bars,
        'title': 'Бары'
    }
    return render(request, 'Bars/index.html', context=context)

def index_dark(request):
    bars = Bars.objects.all()
    context = {
        'bars': bars,
        'title': 'Бары'
    }
    return render(request, 'Bars/index_dark.html', context=context)

def about(request):
    return render(request, 'Bars/about_us.html')

def about_dark(request):
    return render(request, 'Bars/about_us_dark.html')


def register(request):
    if request.method == "POST":
        register_form = UserRegisterForm(request.POST)
        login_form = UserLoginForm(data=request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('register')
        elif login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('home')
    else:
        register_form = UserRegisterForm()
    return render(request, 'Bars/reg.html', {"form": register_form})

def register_dark(request):
    if request.method == "POST":
        register_form = UserRegisterForm(request.POST)
        login_form = UserLoginForm(data=request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('register_dark')
        elif login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('home_dark')
    else:
        register_form = UserRegisterForm()
    return render(request, 'Bars/reg_dark.html', {"form": register_form})

def user_logout(request):
    logout(request)
    return redirect('register')

def user_logout_dark(request):
    logout(request)
    return redirect('register_dark')
