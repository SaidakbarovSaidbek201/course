"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="YouTube API",
        default_version='v1',
        description="YouTube uchun qilingan testoviy API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@myapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # DRF login va logout sahifasi
    path('api/v1/auth/', include('rest_framework.urls')),
    # Token orqali autentifikatsiya qilish
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    # Ro‘yxatdan o‘tish
    path('api/v1/dj-rest-auth/registration/', 
    include('dj_rest_auth.registration.urls')),


]
