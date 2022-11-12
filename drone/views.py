from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'drone/index.html')

def check_drone_status(request):
    return render(request,'drone/check_drone_status.html')