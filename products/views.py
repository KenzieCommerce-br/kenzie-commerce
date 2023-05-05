from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsVendorAdminOrReadOnly
from .models import Product
from .serializers import ProductSerializer


class ProductView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsVendorAdminOrReadOnly]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = Product.objects.all()
        category = self.request.query_params.get("category")
        name = self.request.query_params.get("name")
        if category is not None:
            queryset = queryset.filter(category=category)
            return queryset
        elif name is not None:
            queryset = queryset.filter(name=name)
            return queryset
        return queryset


class DetailProductView(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsVendorOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
