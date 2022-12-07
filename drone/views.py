from django.shortcuts import render
import pyrebase
import requests
 
config = {
    "apiKey": "AIzaSyBhIVn3prbiF0XWw5xqV2UtnSFVcm6Qocg",
    "authDomain": "drone-system-iot.firebaseapp.com",
    "databaseURL": "https://drone-system-iot-default-rtdb.firebaseio.com",
    "projectId": "drone-system-iot",
    "storageBucket": "drone-system-iot.appspot.com",
    "messagingSenderId": "101869826123",
    "appId": "1:101869826123:web:d11da3d9d6566fd54b5dce",
    "measurementId": "G-H6MH5YHNXY"

  }
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()
from django.http import HttpResponse

# Create your views here.


def index(request):

    # latitude = database.child('Data').child('latitude').stream(stream_handler)
    # longitude = database.child('Data').child('longitude').stream(stream_handler)
    # data = database.child('gps').child('coordinates').get()
    # latitude = 
    longitude = database.child('Data').child('longitude').get().val()

    return render(request,"drone/index.html",{"latitude":latitude,"longitude":longitude,"latitude_direction":latitude_direction,"longitude_direction":longitude_direction})

# def index(request):
#     return render(request,'drone/index.html')

def check_drone_status(request):
    return render(request,'drone/check_drone_status.html')


def stream_handler(message):
    # Print the updated data to the console
    print(message["data"])

def home_page(request):
    return render(request,'drone/home.html')

def login_page(request):
    return render(request,'drone/login.html')

def signup_page(request):
    return render(request,'drone/signup.html')

