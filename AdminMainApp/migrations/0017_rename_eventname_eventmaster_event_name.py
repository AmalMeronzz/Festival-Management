# Generated by Django 4.0 on 2023-12-11 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdminMainApp', '0016_eventmaster_eventname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventmaster',
            old_name='EventName',
            new_name='event_name',
        ),
    ]
