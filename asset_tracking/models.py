from django.db import models

# Define models for the asset tracking app


# Model to represent a company
class Company(models.Model):
    company_name = models.CharField(max_length=255)

    def __str__(self):
        # Return a string representation of the Company instance
        return f"{self.id} - {self.company_name}"

# Model to represent an employee
class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=255)

    def __str__(self):
        # Return a string representation of the Employee instance
        return f"{self.id} - {self.employee_name} - {self.company}"
    
# Model to represent a device
class Device(models.Model):
    device_name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        # Return a string representation of the Device instance
        return f"{self.id} - {self.device_name} - {self.company}"
    
# Model to represent the log of device transactions
class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    checkout_time = models.DateTimeField()
    return_time = models.DateTimeField(null=True)
    condition_out = models.TextField()
    condition_returned = models.TextField(null=True)

    def __str__(self):
        # Return a string representation of the DeviceLog instance
        return f"{self.id} - {self.device} - {self.employee}"
