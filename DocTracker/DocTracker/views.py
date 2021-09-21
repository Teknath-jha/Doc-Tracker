import os
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.views import generic
from django.views.generic.base import View
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import check_password


class landingPage(View):

    def get(self, request, template_name='landingPage.html'):
        try:
            message = {'message': 'message'}
            message['message'] = 'nothing'
        except:
            message = {'message': 'message'}
            message['message'] = 'nothing'
        return render(request, template_name, message)


class about(View):
    def get(self, request, template_name = 'about.html'):
        return render(request, template_name)

class avi(View):
    def get(self, request, template_name = 'avi.html'):
        return render(request, template_name)
