from rest_framework import serializers
from carts.models import Cart, CartItem
from products.models import Product

from products.serializers import ProductSerializer


class CartItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = CartItem
        fields = ["id", "product", "quantity"]
        read_only_fields = ["id"]


class CartSerializer(serializers.ModelSerializer):
    products = CartItemSerializer(many=True, write_only=True)

    class Meta:
        model = Cart
        fields = ["id", "user_id", "total_value", "products"]
        read_only_fields = ["id", "total_value"]

    def create(self, validated_data: dict):
        products_data = validated_data.pop("products")
        cart = Cart.objects.create(**validated_data)

        for product_data in products_data:
            product = product_data.pop("product")
            CartItem.objects.create(cart=cart, product=product, **product_data)

        return cart
