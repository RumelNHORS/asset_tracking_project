from django.shortcuts import render
from rest_framework import generics
from asset_tracking import models
from asset_tracking import serializers

# Define views for handling API requests

class CompanyListCreateView(generics.ListCreateAPIView):
    # View to list and create companies
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer

# View to list and create employees
class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer

# View to list and create devices
class DeviceListCreateView(generics.ListCreateAPIView):
    queryset = models.Device.objects.all()
    serializer_class = serializers.DeviceSerializer