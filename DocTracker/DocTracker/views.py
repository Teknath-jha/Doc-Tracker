import pyrebase
import os
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.views import generic
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth.hashers import check_password

config = {
    "apiKey": "AIzaSyC3DKMArlBjbnv2l77aUUsgAi_-bR9bFD8",
    "authDomain": "wce-doc-tracker.firebaseapp.com",
    "databaseURL": "https://wce-doc-tracker-default-rtdb.firebaseio.com",
    "projectId": "wce-doc-tracker",
    "storageBucket": "wce-doc-tracker.appspot.com",
    "messagingSenderId": "127465159856",
    "appId": "1:127465159856:web:1f4f662785411fc525cf75"
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()


class landingPage(View):

    def get(self, request, template_name='landingPage.html'):
        pName = database.child("Data").child('Name').get().val()
        pRoll = database.child("Data").child('Roll').get().val()
        pStd = database.child("Data").child('std').get().val()
        try:
            message = {'message': 'message'}
            message['message'] = pName+' '+pRoll+' '+pStd
            print(message)
        except:
            message = {'message': 'message'}
            message['message'] = 'nothing'
        return render(request, template_name)


class about(View):
    def get(self, request, template_name='about.html'):
        return render(request, template_name)

class login(View):
    def get(self, request, template_name='login.html'):
        return render(request, template_name)

class signup(View):
    def get(self, request, template_name='signup.html'):
        return render(request, template_name)

