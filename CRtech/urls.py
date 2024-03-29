"""CRtech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import re_path
from WebUtility.views import data_his as data_his_view
from WebUtility.views import disp_his as disp_his_view
from WebUtility.views import index as index
from WebUtility.views import insert_data_his as insert_data_his_view
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^datahis/$',data_his_view),
    re_path(r'^showdata/$',disp_his_view),
    re_path(r'^$',index),
    re_path(r'^insert/$',insert_data_his_view),
]
