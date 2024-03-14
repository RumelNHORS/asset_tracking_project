from rest_framework import serializers
from asset_tracking import models

# Define serializers to convert models to JSON format


# Serializer for Company model
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = '__all__'

# Serializer for Employee model
class EmployeeSerializer(serializers.ModelSerializer):
    company_name = serializers.SerializerMethodField()
    class Meta:
        model = models.Employee
        # fields = '__all__'
        fields = ['id', 'employee_name', 'company', 'company_name']
    
    # Include the company name
    def get_company_name(self, obj):
        return obj.company.company_name

# Serializer for Device model
class DeviceSerializer(serializers.ModelSerializer):
    company_name = serializers.SerializerMethodField()
    class Meta:
        model = models.Device
        # fields = '__all__'
        fields = ['id', 'device_name', 'company', 'company_name']

    # Include the company name
    def get_company_name(self, obj):
        return obj.company.company_name

# Serializer for DeviceLog model
class DeviceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DeviceLog
        fields = '__all__'