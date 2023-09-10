from django.shortcuts import render
from rest_framework import generics
from .models import GymModel
from .serializers import GymSerializers


class GymApiView(generics.ListCreateAPIView):
    queryset = GymModel.objects.all()
    serializer_class = GymSerializers


class UpdateGymApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GymModel.objects.all()
    serializer_class = GymSerializers


