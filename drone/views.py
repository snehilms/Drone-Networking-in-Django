from django.shortcuts import render
import pyrebase
import requests

import sys, errno  
# from  firebase import firebase

import firebase_admin
from firebase_admin import credentials,db
from threading import Thread

cred = credentials.Certificate("D:/droneNetworking/drone-system-iot-firebase-adminsdk-selsr-36021455d8.json")
firebase_admin.initialize_app(cred,{
	'databaseURL':"https://drone-system-iot-default-rtdb.firebaseio.com"
	})
# firebase = firebase.FirebaseApplication('https://drone-system-iot-default-rtdb.firebaseio.com',None)


# config = {
# "apiKey": "AIzaSyBhIVn3prbiF0XWw5xqV2UtnSFVcm6Qocg",
#   "authDomain": "drone-system-iot.firebaseapp.com",
#   "databaseURL": "https://drone-system-iot-default-rtdb.firebaseio.com",
#   "projectId": "drone-system-iot",
#   "storageBucket": "drone-system-iot.appspot.com",
#   "messagingSenderId": "101869826123",
#   "appId": "1:101869826123:web:d11da3d9d6566fd54b5dce",
#   "measurementId": "G-H6MH5YHNXY"
#   }
# firebase=pyrebase.initialize_app(config)
# authe = firebase.auth()
# database=firebase.database()

ref = db.reference('gps')
# data=dict()
# def on_data_added(event):
#     print(event.data)
#     latitude = data['Latitude']
#     longitude = data['Longitude']
    
    # data = event.data.popitem()[1]
    # print("data: ",data['Latitude'])
    

# def listen_for_data():
#     try:
#         ref.listen(on_data_added)
#     except KeyboardInterrupt:
#         print("Stopping data listening...")

# def index(request):
#     listen_thread = Thread(target=listen_for_data)
#     listen_thread.start()
#     return render(request,"drone/index.html")
def index(request):
    try:
        data = ref.order_by_child('timestamp').limit_to_last(1).get()
        data_fields = data[list(data.keys())[0]]
        latitude = data_fields['Latitude']
        longitude = data_fields['Longitude']
        timestamp = data_fields['timestamp']
        print("Latitude:", latitude)
        print("Longitude:", longitude)
        print('Timestamp:',timestamp)
        # return final_data
        # ref.listen(on_data_added)
    except KeyboardInterrupt:
        print("Stopping data listening...")
    return render(request,"drone/index.html",{"Latitude":latitude,"Longitude":longitude,"timestamp":timestamp})
    

def check_drone_status(request): 
    return render(request,'drone/check_drone_status.html')



def home_page(request):
    return render(request,'drone/home.html')

def login_page(request):
    return render(request,'drone/login.html')

def signup_page(request):
    return render(request,'drone/signup.html')

