# Generated by Django 4.0 on 2024-01-17 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminMainApp', '0029_rename_college_id_participantregistrationheader_college_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participantregistrationchild',
            name='participant_id_card',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
