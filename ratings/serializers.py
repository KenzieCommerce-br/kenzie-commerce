from rest_framework import serializers
from products.models import Product
from .models import Rating
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']
        read_only_fields = ['username']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'category']
        read_only_fields = ['name', 'category']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'comments', 'stars', 'product_id', 'order_id', 'user_id']
        read_only_fields = ['id', 'product_id', 'order_id', 'user_id']


class AllRatingSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    user = UserSerializer()

    class Meta:
        model = Rating
        fields = ['comments', 'stars', 'product', 'user']
        read_only_fields = ['comments', 'stars', 'product', 'user']
