from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from .permissions import IsVendorOrReadOnly
from .models import Product
from .serializers import ProductSerializer


class ProductView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsVendorOrReadOnly]
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DetailProductView(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsVendorOrReadOnly]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
