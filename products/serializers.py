from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        validators=[UniqueValidator(queryset=Product.objects.all())]
    )

    class Meta:
        model = Product
        read_only_fields = ["id", "available"]
        fields = ["id", "price", "image", "name", "stock", "category", "available"]


class UpdateProductSerializer(serializers.ModelSerializer):
    available = serializers.SerializerMethodField()

    def get_available(self, obj: Product):
        if obj.stock == 0:
            return obj.available == False
        return obj.available == True

    def update(self, instance: Product, validated_data: dict) -> Product:
        stock = validated_data.get("stock")
        setattr(instance, "stock", stock)
        instance.save()
        return instance

    class Meta:
        model = Product
        read_only_fields = ["id", "price", "name", "category", "available"]
        fields = ["id", "price", "name", "stock", "category", "available"]
