# Generated by Django 4.0 on 2024-02-17 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminMainApp', '0032_menuheader_eventmaster_max_registration_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuchild',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='menuheader',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
