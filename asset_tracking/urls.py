from django.urls import path
from asset_tracking import views

# Define URL patterns for API endpoints

urlpatterns = [
    path('companies/', views.CompanyListCreateView.as_view(), name='company_list_create'),
    path('employees/', views.EmployeeListCreateView.as_view(), name='employee_list_create'),
    path('devices/', views.DeviceListCreateView.as_view(), name='device_list_create'),
    path('logs/', views.DeviceLogListCreateView.as_view(), name='device-log-list-create'),
]