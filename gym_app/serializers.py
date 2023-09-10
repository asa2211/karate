from rest_framework import serializers
from .models import GymModel


class GymSerializers(serializers.ModelSerializer):
    class Meta:
        model = GymModel
        fields = ('name', 'address', 'phone', 'coach', 'email', 'open_time')
