# Generated by Django 4.0 on 2023-12-05 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdminMainApp', '0013_alter_festivalmasterheader_institution_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='festivalmasterheader',
            name='institution_id',
        ),
    ]
