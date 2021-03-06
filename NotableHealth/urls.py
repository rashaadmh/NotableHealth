"""django1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from doctor.views import get_doctors, get_appointment_for_doctor, delete_appointment, create_appointment, create_doctor
from sample_model.views import test_view, test_view_with_body

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_doctors/', get_doctors),
    path('get_appointments/', get_appointment_for_doctor),
    path('delete_appointment/', delete_appointment),
    path('create_appointment/', create_appointment),
    path('create_doctor/', create_doctor)
]
