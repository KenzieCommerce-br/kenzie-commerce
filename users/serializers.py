from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True)
    is_seller = serializers.BooleanField(allow_null=True, default=False)

    def create(self, validated_data: dict) -> User:
        is_admin = validated_data.get("is_admin", False)
        if is_admin:
            validated_data["is_seller"] = True
            return User.objects.create_superuser(**validated_data)
        else:
            return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',
            'is_admin',
            'is_seller',
        ]
