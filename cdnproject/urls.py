"""cdnproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_jwt.views import obtain_jwt_token,verify_jwt_token
api_urlpatterns = [
    path('', include('map.api_urls')),
    path('auth/', obtain_jwt_token),
    path('auth/verify/', verify_jwt_token),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("",
    #     TemplateView.as_view(template_name="application.html"),
    #     name="app",
    # ),

    path('api/1.0/', include(api_urlpatterns)),  # api/1.0/としてapi一覧を登録
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)