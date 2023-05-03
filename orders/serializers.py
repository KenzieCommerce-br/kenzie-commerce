from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id', 'status', 'hour', 'user_id']

        extra_kwargs = {'id': {'read_only': True}, 'user_id': {'read_only': True}}