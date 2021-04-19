from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics

from driver_app.models import Advice
from driver_app.serializers import AdviceSerializer


class AdviceAPIView(generics.ListCreateAPIView):
    queryset = Advice.objects.all().order_by('?')
    serializer_class = AdviceSerializer

class AdviceDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Advice.objects.all()
    serializer_class = AdviceSerializer

