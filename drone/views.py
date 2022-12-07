from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request,'drone/index.html')

def check_drone_status(request):
    return render(request,'drone/check_drone_status.html')

def home_page(request):
    return render(request,'drone/home.html')

def login_page(request):
    return render(request,'drone/login.html')

def signup_page(request):
    return render(request,'drone/signup.html')