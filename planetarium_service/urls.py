from django.contrib import admin
from django.urls import path, include
from planetarium_service.views import api_root

urlpatterns = [
    path('', api_root, name='api-root'),
    path("api/user/", include("user.urls", namespace="user")),
    path("api/planetarium/", include("planetarium.urls", namespace="planetarium")),
]