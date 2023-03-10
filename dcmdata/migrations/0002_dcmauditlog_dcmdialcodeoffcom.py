# Generated by Django 4.1.5 on 2023-01-17 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dcmdata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DcmAuditLog',
            fields=[
                ('id', models.FloatField(primary_key=True, serialize=False)),
                ('file_id', models.CharField(blank=True, max_length=100, null=True)),
                ('file_name', models.CharField(blank=True, max_length=100, null=True)),
                ('file_type', models.FloatField(blank=True, max_length=20, null=True)),
                ('source', models.CharField(blank=True, max_length=100, null=True)),
                ('destination', models.CharField(blank=True, max_length=100, null=True)),
                ('process_config_id', models.FloatField(blank=True, max_length=20, null=True)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('error', models.CharField(blank=True, max_length=100, null=True)),
                ('record_count', models.FloatField(blank=True, max_length=20, null=True)),
                ('file_extn', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'DCM_AUDIT_LOG',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DcmDialCodeOffcom',
            fields=[
                ('number_range_skey', models.FloatField(primary_key=True, serialize=False)),
                ('nms_number_block', models.CharField(blank=True, max_length=100, null=True)),
                ('block_status', models.CharField(blank=True, max_length=20, null=True)),
                ('cp_name', models.CharField(blank=True, max_length=500, null=True)),
                ('geographic_number_length', models.CharField(blank=True, max_length=100, null=True)),
                ('non_geo_number_length', models.CharField(blank=True, max_length=100, null=True)),
                ('allocation_date', models.DateTimeField(blank=True, null=True)),
                ('notes', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'db_table': 'DCM_DIAL_CODE_OFFCOM',
                'managed': False,
            },
        ),
    ]
