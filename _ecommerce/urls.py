from django.contrib import admin
from django.urls import path, include
import products

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/",
        include("users.urls", "products.urls"),
    ),
]
