
from django.contrib import admin
from django.urls import path, include


#導航到project 的url
urlpatterns = [
    path('admin/', admin.site.urls ),
    path('',include('projects.urls'))
]
