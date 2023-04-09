from django.contrib import admin
from django.urls import path, include
from project.views import *


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("djangogp.urls")),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
]
