from rest_framework.routers import DefaultRouter
from . import api_views
from django.urls import path
from . import views

"""
PostData_router = DefaultRouter()
PostData_router.register(r'', api_views.PostDataViewSet)
"""
urlpatterns = [
    path('PostData/', api_views.PostDataViewSet.as_view(), name= 'post_data'),
    path('register/', api_views.AuthRegister.as_view(),name= 'register'),
    path('GetUser/',api_views.AuthGet.as_view(),name='get_user'),
]