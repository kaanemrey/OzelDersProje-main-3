from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from datetime import date,datetime
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
 

def login_page(request):
    sayfa = 'login'
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'Böyle bir kullanıcı ismi bulunmuyor')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Home')
        else:
            messages.error(request, 'Yanlış Şifre')
    context = {'sayfa': sayfa}
    return render(request, 'Log-Sign.html', context)


def logout_user(request):
    logout(request)
    return redirect('Home')


def register_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')
    else:
        form = UserCreationForm()
    return render(request, 'Log-Sign.html', {'form': form})


def MainPage(request):
    return render(request, 'MainPage.html')


def OzelDers(request):
    return render(request, 'OzelDers.html')


def biz_kimiz(request):
    return render(request, 'hakkımızda.html')


def DersTalepleri(request):
    return render(request, 'DersTalepleri.html')


def Matematik(request):
    return render(request, 'matematik.html')

def Python(request):
    return render(request, 'python.html')

def Fizik(request):
    return render(request, 'fizik.html')

def Gitar(request):
    return render(request, 'gitar.html')