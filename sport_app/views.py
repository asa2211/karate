from django.shortcuts import render
from rest_framework import generics
from .serializers import CustomUserSerializers
from .models import CustomUser


class SignUpApiView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializers
