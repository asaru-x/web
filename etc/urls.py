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
#from django.urls import path, re_path
from django.conf.urls import url
from qa.views import new_q, popular_q, common_handler, question_page

'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', new_q, name='new_questions'),
    path('new/', new_q, name='new_questions'),
    path('popular/', popular_q, name='popular_questions'),
    path('login/', common_handler),
    path('signup/', common_handler),
    path('question/<str:slug>/', question_page)
]
'''
urlpatterns = [
    url('^admin/$', admin.site.urls),
    url('^$', new_q, name='new_questions'),
    url('^new/$', new_q, name='new_questions'),
    url('^popular/$', popular_q, name='popular_questions'),
    url('^login/$', common_handler),
    url('^signup/$', common_handler),
    url('^question/<str:slug>/$', question_page)
]