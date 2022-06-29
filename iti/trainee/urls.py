from django.urls import path , include
from .views import *



urlpatterns = [
path('',listuser),
path('update/<id>',Update,name='updateuser'),
path('delete/<id>',Delete,name='deleteuser')
]