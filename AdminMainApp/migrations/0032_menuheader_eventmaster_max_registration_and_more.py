# Generated by Django 4.0 on 2024-02-17 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdminMainApp', '0031_alter_eventmaster_event_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuHeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=20, null=True)),
                ('modified_on', models.DateTimeField(null=True)),
                ('modified_by', models.CharField(max_length=20, null=True)),
            ],
        ),

        migrations.AlterField(
            model_name='participantregistrationheader',
            name='college_name',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.CreateModel(
            name='MenuChild',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=20, null=True)),
                ('modified_on', models.DateTimeField(null=True)),
                ('modified_by', models.CharField(max_length=20, null=True)),
                ('menu_header_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AdminMainApp.menuheader')),
            ],
        ),
    ]