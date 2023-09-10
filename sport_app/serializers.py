from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'role', 'phone', 'first_name')

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            password=validated_data['password'],
            role=validated_data.get('role', 1),
            phone=validated_data.get('phone'),
            first_name=validated_data.get('first_name')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
