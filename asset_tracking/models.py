from django.db import models

# Define models for the asset tracking app

class Company(models.Model):
    # Model to represent a company
    company_name = models.CharField(max_length=255)

    def __str__(self):
        # Return a string representation of the Company instance
        return f"{self.id} - {self.company_name}"

class Employee(models.Model):
    # Model to represent an employee
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=255)

    def __str__(self):
        # Return a string representation of the Employee instance
        return f"{self.id} - {self.employee_name} - {self.company}"
