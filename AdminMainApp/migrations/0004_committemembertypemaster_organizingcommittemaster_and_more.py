# Generated by Django 4.0 on 2023-11-17 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdminMainApp', '0003_festivalmasterheader'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommitteMemberTypeMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('committe_member_type', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=20, null=True)),
                ('modified_on', models.DateTimeField(null=True)),
                ('modified_by', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrganizingCommitteMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('committe_member_name', models.CharField(max_length=70)),
                ('committe_member_phone', models.CharField(blank=True, max_length=15, null=True)),
                ('committe_member_photo', models.CharField(blank=True, max_length=50, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=20, null=True)),
                ('modified_on', models.DateTimeField(null=True)),
                ('modified_by', models.CharField(max_length=20, null=True)),
                ('committe_member_type_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='AdminMainApp.committemembertypemaster')),
                ('department_master_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminMainApp.departmentmaster')),
                ('festival_master_header_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminMainApp.festivalmasterheader')),
            ],
        ),
        migrations.CreateModel(
            name='FestivalMasterChild',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_start_date', models.DateField(blank=True, null=True)),
                ('registration_end_date', models.DateField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=20, null=True)),
                ('modified_on', models.DateTimeField(null=True)),
                ('modified_by', models.CharField(max_length=20, null=True)),
                ('festival_master_header_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminMainApp.festivalmasterheader')),
            ],
        ),
    ]
