from django.contrib import admin
from asset_tracking import models

# Register models here.
admin.site.register(models.Company)
admin.site.register(models.Employee)
admin.site.register(models.Device)
admin.site.register(models.DeviceLog)
