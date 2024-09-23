from django.urls import path
from . import views


app_name = 'menu'

urlpatterns = [
    path('' , views.food_list , name = 'list'),
    path('<slug:slug>/' , views.food_detail , name = 'detail'),
]

