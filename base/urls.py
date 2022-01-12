from django.urls import path
# import view file
from . import views

urlpatterns =[
    path('',views.home,name="home"),
    path('room/',views.room,name="room"),
]