from django.urls import path

from . import views


app_name = 'booking'
url_patterns = [
    path('', views.index, name = 'index'),
    path('login', views.login, name = 'login')
]