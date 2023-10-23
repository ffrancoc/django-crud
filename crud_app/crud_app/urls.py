from django.contrib import admin
from django.urls import path, include

urlpatterns = [    
    path('crud/', include('main_app.urls')),
]
