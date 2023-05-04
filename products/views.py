from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from users.permissions import IsVendorOrReadOnly
from .models import Product
from .serializers import ProductSerializer


class ProductView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsVendorOrReadOnly]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        category = self.request.query_params.get("category")
        name = self.request.query_params.get("name")
        queryset = Product.objects.all()
        if category is not None:
            queryset = queryset.filter(category=category)
            return queryset
        elif name is not None:
            queryset = queryset.filter(name=name)
            return queryset


class DetailProductView(RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsVendorOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
