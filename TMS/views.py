from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TmsSerializer
from .models import TMS

# Create your views here.

class TmsView(viewsets.ModelViewSet):
    serializer_class = TmsSerializer
    queryset = TMS.objects.all()