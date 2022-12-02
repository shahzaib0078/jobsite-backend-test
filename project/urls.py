"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter

from accounts.views import UserViewSet, UserCreateViewSet
from advertisements.views import AdvertisementViewSet
from jobs.views import JobViewSet
from websites.views import WebsiteViewSet


schema_view = get_schema_view(
    openapi.Info(
        title="Job Portal Backdoor",
        default_version="v1",
        description="Backend APIs",
    ),
    public=True,
    permission_classes=(AllowAny,),
)

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"users", UserCreateViewSet)
router.register(r"jobs", JobViewSet)
router.register(r"advertisements", AdvertisementViewSet)
router.register(r"websites", WebsiteViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "ui", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("api/v1/", include(router.urls)),
]
