# Generated by Django 4.0 on 2023-12-14 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminMainApp', '0017_rename_eventname_eventmaster_event_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventprizemaster',
            name='cash_amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='eventprizemaster',
            name='event_score',
            field=models.IntegerField(null=True),
        ),
    ]