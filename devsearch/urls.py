
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 


#導航到project 的url
urlpatterns = [
    path('admin/', admin.site.urls ),
    path('projects/',include('projects.urls')), #開頭為空白的會被丟到projects.url 處理
    path('',include('users.urls')), # #開頭為users的會被丟到users.url 處理
   
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)