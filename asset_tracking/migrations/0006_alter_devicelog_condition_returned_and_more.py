# Generated by Django 5.0.3 on 2024-03-14 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset_tracking', '0005_devicelog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicelog',
            name='condition_returned',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='devicelog',
            name='return_time',
            field=models.DateTimeField(null=True),
        ),
    ]