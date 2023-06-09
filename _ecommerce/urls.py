from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("users.urls")),
    path("api/", include("products.urls")),
    path("api/", include("addresses.urls")),
    path("api/", include("orders.urls")),
    path("api/", include("order_seller.urls")),
    path("api/", include("carts.urls")),
    path("api/", include("ratings.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/swagger/", SpectacularSwaggerView.as_view(url_name="schema"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

