from django.db.models import Q
from django.shortcuts import render
from rest_framework import generics
from .models import GymModel
from .serializers import GymSerializers


class GymApiView(generics.ListCreateAPIView):
    queryset = GymModel.objects.all()
    serializer_class = GymSerializers

    def get_queryset(self):
        queryset = GymModel.objects.all()
        coach_name = self.request.query_params.get('coach_name')

        if coach_name:
            queryset = queryset.filter(
                Q(coach__first_name__icontains=coach_name) |
                Q(coach__last_name__icontains=coach_name)
            )

        return queryset


class UpdateGymApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GymModel.objects.all()
    serializer_class = GymSerializers
