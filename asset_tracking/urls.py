from django.urls import path
from asset_tracking import views

# Define URL patterns for API endpoints

urlpatterns = [
    path('companies/', views.CompanyListCreateView.as_view(), name='company_list_create'),

]