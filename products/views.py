from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsVendorOrReadOnly
from .models import Product
from .serializers import ProductSerializer


class ProductView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsVendorOrReadOnly]
