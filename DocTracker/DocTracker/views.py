import pyrebase
import os
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import auth
from django.views import generic
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth.hashers import check_password
from django.core.mail import send_mail
from django.core.mail import EmailMessage

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

    def post(self, request, template_name='login.html'):
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = authe.sign_in_with_email_and_password(email, password)
            print(user)
            session_id = user['idToken']
            request.session['uid'] = str(session_id)
            msg={}
            msg['email']=email
            msg['session_id'] = session_id
            msg['local_id'] = user['localId']
            return render(request, 'firstClerk.html', msg)
        except:
            err = {}
            err['error_message'] = "Invalid credentials"
            return render(request, 'login.html', err)


def logout_user(request):
    auth.logout(request)
    message = {}
    message['loggedOut'] = "Successfully Logged Out"
    return render(request, 'login.html', message)


class signup(View):
    def get(self, request, template_name='signup.html'):
        return render(request, template_name)

    def post(self, request, template_name='signup.html'):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phoneNumber = request.POST.get('phoneNumber')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # confPassword = request.POST.get('conf_password')

        # if password != confPassword:
        #     err = {'error_message': "Password don't match. Please Try Again."}
        #     return render(request, 'signup.html', err)

        try:
            user = authe.create_user_with_email_and_password(email, password)
            uid = user['localId']
            data = {"First_name": first_name,
                         "Last_name": last_name,
                         "email":email,
                         "phoneNumber": phoneNumber, 
                         "status": "1"}
            database.child("users").child(uid).child("details").set(data)
            return render(request, 'login.html')
        except:
            err = {}
            err['error_message1'] = "Account with this Username or Email already exists."
            err['error_message2'] = "Password length must be atleast 6 ."
            return render(request, template_name, err)


class create(View):
    def get(self, request, template_name='create.html'):
        return render(request, template_name)

    def post(self, request, template_name='login.html'):
        import time
        from datetime import datetime, timezone
        import pytz
        try:
            tz = pytz.timezone('Asia/Kolkata')
            time_now = datetime.now(timezone.utc).astimezone(tz)
            millis = int(time.mktime(time_now.timetuple()))
            print(str(millis))
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            phoneNumber = request.POST.get('phoneNumber')
            email = request.POST.get('email')
            msg1 = {}
            msg1['email']=email
            msg1['phoneNumber'] = phoneNumber
            # password = request.POST.get('password')
            idtoken = request.session['uid']
            a = authe.get_account_info(idtoken)
            a = a['users']
            a = a[0]
            a = a['localId']
            # msg1['local_id'] = a['localId']
            print(str(a))
            data = {
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "phoneNumber": phoneNumber,
            }
            print("****------------***********")
            database.child('users').child(a).child(
                'reports').child(millis).set(data)
            print("***111111---Saved---11111111*******")
            

            send_mail(
                'Doc Tracker ',
                'Welcome to doc tracker your doc is under processes',
                'farookdio72@gmail.com',
                ['jhateknath64@gmail.com',email,'aditsan44@gmail.com',],

            )
            print("--------Sent--------")
            return render(request, 'create.html',msg1)
        except:
            print("-----------Not sent--------------")
            err = {}
            # err['error_message1'] = "Account with this Username or Email already exists."
            err['error_message1'] = "Fails to send email message."
            # err['error_message2'] = "Password length must be atleast 6 ."
            return render(request, 'firstClerk.html', err)
