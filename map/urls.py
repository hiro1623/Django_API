from django.conf.urls import url
from django.urls import path,include
from . import views

app_name = "mapApp"
urlpatterns = [
    path('', views.map_TownHero, name='map_TownHero'),
    path('delete/', views.delete, name='delete'),
    path('post/', views.post, name='post'),
    
]

