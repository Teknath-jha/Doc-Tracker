"""DocTracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landingPage.as_view(), name="landingPage"),
    path('about/',views.about.as_view(),name="about"),
    path('login/',views.login.as_view(),name="login"),
    path('logout/',views.logout_user,name="logout"),
    path('signup/',views.signup.as_view(),name="signup"),
    path('firstClerk/',views.login.as_view(),name="firstClerk"),
    path('staffLandingPage/',views.StaffCommonPage.as_view(),name="staffLandingPage"),
    path('staffWork/',views.StaffWork.as_view(),name="staffWork"),
    path('desk1/',views.login.as_view(),name="desk1"),
    path('desk2/',views.login.as_view(),name="desk2"),
    path('desk3/',views.login.as_view(),name="desk3"),
    path('create/',views.create.as_view(),name="create"),
    path('report/',views.report.as_view(),name="report"),
]


