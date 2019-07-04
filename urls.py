from django.contrib import admin
from django.urls import include, path

from . import views
urlpatterns = [
        path('startscreen', views.start_screen,name='login'),
        path('createworld01', views.create_world_01, name='create_world_01'),
        path('showworld01', views.show_world_01, name='show_world_01')
        ]
