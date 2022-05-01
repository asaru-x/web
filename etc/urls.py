"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, re_path
#from django.conf.urls import url
from qa.views import handler

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', handler),
    re_path(r'^login/$', handler),
    re_path(r'^signup/$', handler),
    re_path(r'^new/$', handler),
    re_path(r'^popular/$', handler),
    re_path(r'^ask/$', handler),
    re_path(r'^question/', handler),
]
'''
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', handler),
    url(r'^login/$', handler),
    url(r'^signup/$', handler),
    url(r'^new/$', handler),
    url(r'^popular/$', handler),
    url(r'^ask/$', handler),
    url(r'^question/', handler),
]
'''