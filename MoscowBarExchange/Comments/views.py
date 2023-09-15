from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

from .models import Comments
from Bars.models import Bars
from .forms import UserRegisterForm, UserLoginForm, CommentsForm

# Create your views here.
def index(request, bar_id):
    comments = Comments.objects.filter(bar_id=bar_id)
    bar = Bars.objects.get(pk=bar_id)
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.bar_id = bar.pk
            form.save()
            return redirect('home')
    else:
        form = CommentsForm()
    context = {
        'bar': bar,
        'comments': comments,
        'form': form,
    }
    return render(request, 'Comments/index.html', context=context)

def index_dark(request, bar_id):
    comments = Comments.objects.filter(bar_id=bar_id)
    bar = Bars.objects.get(pk=bar_id)
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.bar_id = bar.pk
            form.save()
            return redirect('home_dark')
    else:
        form = CommentsForm()
    context = {
        'bar': bar,
        'comments': comments,
        'form': form,
    }
    return render(request, 'Comments/index_dark.html', context=context)

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
