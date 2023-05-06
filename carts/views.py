from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    GenericAPIView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from django.db.models import F
from django.shortcuts import get_object_or_404

from .permissions import IsClientOwnerOrAdmin
from products.models import Product
from .serializers import CartSerializer
from .models import Cart, CartItem


class CartView(GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsClientOwnerOrAdmin]

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
        product = get_object_or_404(Product, id=product_id)

        if quantity > product.stock:
            return Response(
                {"error": "Não há estoque suficiente para adicionar ao carrinho."}
            )
        get_product = CartItem.objects.filter(cart=cart, product=product).first()
        if get_product:
            return Response(
                {"error": "Atualize a quantidade do produto pela rota Patch"}
            )
        CartItem.objects.create(
            cart=cart,
            product=product,
            quantity=quantity,
        )

        serializer = self.get_serializer(cart)

        return Response(serializer.data)

    def patch(self, request):
        cart = self.get_object()
        product_id = request.data.get("product")
        quantity = request.data.get("quantity", 1)
        product = get_object_or_404(Product, id=product_id)

        if quantity > product.stock:
            return Response(
                {"error": "Não há estoque suficiente para adicionar ao carrinho."}
            )
        get_product = CartItem.objects.filter(cart=cart, product=product).first()
        if get_product is None:
            return Response(
                status=404,
                data={"error": "Primeiro adicione esse produto ao carrinho."},
            )

        get_quantity = get_product.quantity + quantity

        if quantity > 0:
            if get_quantity > product.stock:
                return Response(
                    {"error": "Não há estoque suficiente para adicionar ao carrinho."}
                )

        if get_product and get_product.quantity > 0:
            get_product.quantity = F("quantity") + quantity
        else:
            get_product.quantity = F("quantity") - quantity
        get_product.save()

        get_product = CartItem.objects.filter(cart=cart, product=product).first()
        if get_product.quantity <= 0:
            get_product.delete()
            serializer = self.get_serializer(cart)
            return Response(serializer.data)

        serializer = self.get_serializer(cart)

        return Response(serializer.data)

    def delete(self, request):
        cart = self.get_object()
        product_id = request.data.get("product")
        product = get_object_or_404(Product, id=product_id)
        cart_item = CartItem.objects.filter(cart=cart, product=product).first()

        if cart_item:
            cart_item.delete()
            serializer = self.get_serializer(cart)
            return Response(serializer.data)
        else:
            return Response(
                status=404, data={"error": "Não tem esse produto no carrinho."}
            )


class CartDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
