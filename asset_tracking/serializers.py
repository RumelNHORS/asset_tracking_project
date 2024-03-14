from rest_framework import serializers
from asset_tracking import models

# Define serializers to convert models to JSON format

class CompanySerializer(serializers.ModelSerializer):
    # Serializer for Company model
    class Meta:
        model = models.Company
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    # Serializer for Employee model
    class Meta:
        model = models.Employee
        fields = '__all__'

# Serializer for Device model
class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Device
        fields = '__all__'

# Serializer for DeviceLog model
class DeviceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DeviceLog
        fields = '__all__'