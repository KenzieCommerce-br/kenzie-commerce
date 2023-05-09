from rest_framework import serializers
from .models import Address


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ['id', 'street', 'number', 'complement', 'zip_code', 'user_id']
        read_only_fields = ['id', 'user_id']


class AddressUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'street', 'number', 'complement', 'zip_code', 'user_id', 'default']
        read_only_fields = ['id', 'user_id']
