from django.urls import path
from . import views

#views.createProject 的意思是 裡面的內容call createProject name 幫忙取名赤

urlpatterns = [
    path('', views.projects, name='projects'),
    path('project/<str:pk>/', views.project, name='project'), 
    path('create-project/',views.createProject,name='create-project'), #這個是網址(url),
    path('update-project/<str:pk>/',views.updateProject,name = 'update-project' ),

    path('delete-project/<str:pk>/',views.deleteProject,name = 'delete-project' ),

]