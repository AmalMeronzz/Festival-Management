# Generated by Django 4.0 on 2024-01-11 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminMainApp', '0024_eventmaster_event_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participantregistrationheader',
            name='college_id',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
