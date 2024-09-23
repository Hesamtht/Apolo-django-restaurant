from django.urls import path
from .views import register, comment

app_name = 'profiles'

urlpatterns = [
    path('', register, name = 'register'),
    path('comment/<slug:slug>/', comment, name = 'comment'),
]
