"""Connecting_Api URL Configuration

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
from django.urls import path,include
from App.views import *
urlpatterns = [
    path('',index,name="index"),
    path('index',index,name="index"),
    path('profile',profile,name="MyProfile"),
    path('ProfileEdit',ProfileEdit,name="myProfileEdit"),
    path('doctorDetails',doctorDetails, name="doctorDetails"),
    path('editDoctorDetails',editDoctorDetails, name='editDoctorDetails'),
    path('weeklyRecord', weeklyRecord, name="WeeklyRecords"),
    path('careTaker',careTaker,name='careTaker'),
    path('editCareTaker',editCareTaker,name='editCareTaker'),
    path('admin/', admin.site.urls),
    path("api_sensor",api_sensor),
    # path("update_sensor",update_sensor),
    path("api_patient",api_patient),
    # path("update_patient",update_patient),
    path("api_care_taker",api_care_taker),
    # path("update_care_taker",update_care_taker),
    path("api_doctor",api_doctor),
    # path("update_doctor",update_doctor)

]
