from rest_framework import serializers
from .models import Rating


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ['id', 'comments', 'stars', 'product_id', 'order_id', 'user_id']

        extra_kwargs = {
            'id': {'read_only': True},
            'product_id': {'read_only': True},
            'order_id': {'read_only': True},
            'user_id': {'read_only': True},
        }
