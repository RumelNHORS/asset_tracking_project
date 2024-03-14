from django.shortcuts import render
from rest_framework import generics
from asset_tracking import models
from asset_tracking import serializers

# Define views for handling API requests

class CompanyListCreateView(generics.ListCreateAPIView):
    # View to list and create companies
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer
