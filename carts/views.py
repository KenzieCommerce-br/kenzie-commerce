from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    GenericAPIView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response

from products.models import Product
from .serializers import CartSerializer
from .models import Cart, CartItem
from django.db.models import F


class CartView(GenericAPIView):
    authentication_classes = [JWTAuthentication]

    serializer_class = CartSerializer

    def get_object(self):
        user = self.request.user
        return Cart.objects.get_or_create(user=user)[0]

    def get(self, request):
        cart = self.get_object()
        serializer = self.get_serializer(cart)
        return Response(serializer.data)

    def post(self, request):
        cart = self.get_object()
        product_id = request.data.get("product")
        quantity = request.data.get("quantity", 1)
        product = Product.objects.get(id=product_id)

        if quantity > product.stock:
            return Response(
                {"error": "Não há estoque suficiente para finalizar o pedido."}
            )
        getProduct = CartItem.objects.filter(cart=cart, product=product).first()
        if getProduct:
            defaults = {"quantity": F("quantity") + quantity}
        else:
            defaults = {"quantity": quantity}
        CartItem.objects.update_or_create(
            cart=cart,
            product=product,
            defaults=defaults,
        )

        serializer = self.get_serializer(cart)

        return Response(serializer.data)


class CartDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
