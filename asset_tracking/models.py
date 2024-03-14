from django.db import models

# Define models for the asset tracking app

class Company(models.Model):
    # Model to represent a company
    company_name = models.CharField(max_length=255)
