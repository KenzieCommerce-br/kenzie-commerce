from rest_framework import serializers
from carts.models import Cart, CartItem
from products.models import Product


class NewCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "price"]


class CartItemSerializer(serializers.ModelSerializer):
    product = NewCartItemSerializer()

    class Meta:
        model = CartItem
        fields = ["id", "product", "quantity"]


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ["id", "items", "total_value"]
