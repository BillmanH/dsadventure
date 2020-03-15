from django.contrib import admin
from django.urls import include, path

from . import views
urlpatterns = [
    path('startscreen', views.start_screen, name='login'),
    path('generateworld', views.create_world_01, name='generate_world'),
    path('showworld03', views.show_world_03, name='show_world03'),
    path('createcharacter', views.create_character, name='create_character'),
    path('coreview', views.core_view, name='core_view'),
    path('charmap', views.char_map, name='char_map'),
    path('eq', views.equipment, name='equipment'),
    path('journal', views.journal, name='journal')]
