# Generated by Django 4.0 on 2024-01-13 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdminMainApp', '0026_participantregistrationchild_participant_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsormaster',
            name='event_master_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AdminMainApp.eventmaster'),
        ),
        migrations.AddField(
            model_name='sponsormaster',
            name='festival_master_header_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AdminMainApp.festivalmasterheader'),
        ),
    ]
