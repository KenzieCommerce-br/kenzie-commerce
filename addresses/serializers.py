from rest_framework import serializers
from .models import Address


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ['id', 'street', 'number', 'complement', 'zip_code', 'user_id']

        extra_kwargs = {'id': {'read_only': True}, 'user_id': {'read_only': True}}
