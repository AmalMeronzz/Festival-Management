# Generated by Django 4.0 on 2024-01-14 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminMainApp', '0027_sponsormaster_event_master_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventmaster',
            name='abbreviation',
            field=models.CharField(max_length=20, null=True),
        ),
    ]