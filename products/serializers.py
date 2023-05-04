from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        validators=[UniqueValidator(queryset=Product.objects.all())]
    )

    class Meta:
        model = Product
        read_only_fields = ["id"]
        fields = ["name", "price", "category", "stock", "avaliable", "image"]
