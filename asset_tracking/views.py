from django.shortcuts import render
from rest_framework import generics
from asset_tracking import models
from asset_tracking import serializers

# Define views for handling API requests


# View to list and create companies
class CompanyListCreateView(generics.ListCreateAPIView):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer

# View for retrieving and updating a Company instance.
class CompanyUpdateView(generics.RetrieveUpdateAPIView):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer


# View to list and create employees
class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer

# View for retrieving and updating an Employee instance
class EmployeeUpdateView(generics.RetrieveUpdateAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer


# View to list and create devices
class DeviceListCreateView(generics.ListCreateAPIView):
    queryset = models.Device.objects.all()
    serializer_class = serializers.DeviceSerializer

# View for retrieving and updating a Device instance.
class DeviceUpdateView(generics.RetrieveUpdateAPIView):
    queryset = models.Device.objects.all()
    serializer_class = serializers.DeviceSerializer


# View to list and create device logs.
class DeviceLogListCreateView(generics.ListCreateAPIView):
    queryset = models.DeviceLog.objects.all()
    serializer_class = serializers.DeviceLogSerializer

# View for retrieving and updating a DeviceLog instance.
class DeviceLogUpdateView(generics.RetrieveUpdateAPIView):
    queryset = models.DeviceLog.objects.all()
    serializer_class = serializers.DeviceLogSerializer