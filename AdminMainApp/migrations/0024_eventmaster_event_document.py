# Generated by Django 4.0 on 2024-01-09 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminMainApp', '0023_eventmaster_event_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventmaster',
            name='event_document',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]