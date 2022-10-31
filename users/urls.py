from nturl2path import url2pathname
from django.urls import path
from . import views

urlpatterns = [
    path('',views.profiles, name="profiles"),
    path('profile/<str:pk>/',views.userProfile, name="user-profile"),

]