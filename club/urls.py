from django.urls import path
from .views import *

app_name = 'club'


urlpatterns = [
    path('' , user_sub , name = 'subscription'),
]
