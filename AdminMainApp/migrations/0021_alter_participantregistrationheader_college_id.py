# Generated by Django 4.0 on 2023-12-22 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminMainApp', '0020_remove_eventprizemaster_cash_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participantregistrationheader',
            name='college_id',
            field=models.IntegerField(null=True),
        ),
    ]
