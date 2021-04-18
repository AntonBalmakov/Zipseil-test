from django.urls import path
from .views import *

name_apps = 'test_app'

urlpatterns = [
    path('', info_user, name='smth')
]