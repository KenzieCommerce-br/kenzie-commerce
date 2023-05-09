from rest_framework import serializers
from orders.models import Order, OrderOptions


class OrderSellerSerializer(serializers.ModelSerializer):

    client_id = serializers.IntegerField(source='user_id', read_only=True)
    order_id = serializers.IntegerField(source='id', read_only=True)
    status = serializers.ChoiceField(choices=OrderOptions)

    class Meta:
        model = Order
        fields = ['order_id', 'status', 'client_id', 'updated_at']

        extra_kwargs = {
            'updated_at': {'read_only': True},
        }


class OrderSellerStatusSerializer(serializers.ModelSerializer):

    client_id = serializers.IntegerField(source='user_id', read_only=True)
    order_id = serializers.IntegerField(source='id', read_only=True)

    class Meta:
        model = Order
        fields = ['order_id', 'status', 'client_id', 'updated_at']

        extra_kwargs = {
            'updated_at': {'read_only': True},
        }
