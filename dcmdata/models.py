# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DcmDialCode(models.Model):
    number_range_skey = models.FloatField(primary_key=True)
    number_range = models.CharField(max_length=100, blank=True, null=True)
    number_range_type = models.CharField(max_length=5, blank=True, null=True)
    number_range_start_date = models.DateField(blank=True, null=True)
    number_range_stop_date = models.DateField(blank=True, null=True)
    number_range_owner_id = models.CharField(max_length=100, blank=True, null=True)
    number_range_owner_name = models.CharField(max_length=100, blank=True, null=True)
    host_name = models.CharField(max_length=30, blank=True, null=True)
    gen_description = models.CharField(max_length=1000, blank=True, null=True)
    bt_charge_band_code = models.CharField(max_length=10, blank=True, null=True)
    cost_category = models.CharField(max_length=5, blank=True, null=True)
    rounding_rule = models.CharField(max_length=10, blank=True, null=True)
    threshold = models.CharField(max_length=100, blank=True, null=True)
    service_description = models.CharField(max_length=50, blank=True, null=True)
    origin_based_rating = models.CharField(max_length=1, blank=True, null=True)
    traffic_type = models.CharField(max_length=10, blank=True, null=True)
    itct_rating_type = models.CharField(max_length=1, blank=True, null=True)
    country_name = models.CharField(max_length=100, blank=True, null=True)
    country_iso_code = models.CharField(max_length=3, blank=True, null=True)
    country_idd_code = models.CharField(max_length=6, blank=True, null=True)
    owner_type = models.CharField(max_length=10, blank=True, null=True)
    source_system = models.CharField(max_length=100, blank=True, null=True)
    insert_timestamp = models.DateTimeField(blank=True, null=True)
    update_timestamp = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    current_flag = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DCM_DIAL_CODE'


class OfcomDialCode(models.Model):
    number_range_skey = models.FloatField(primary_key=True)
    number_block = models.CharField(max_length=1000, blank=True, null=True)
    block_status = models.CharField(max_length=1000, blank=True, null=True)
    number_block_type = models.CharField(max_length=1000, blank=True, null=True)
    cp_name = models.CharField(max_length=1000, blank=True, null=True)
    number_length = models.CharField(max_length=1000, blank=True, null=True)
    allocation_date = models.DateTimeField(blank=True, null=True)
    notes = models.CharField(max_length=1000, blank=True, null=True)
    insert_timestamp = models.DateTimeField(blank=True, null=True)
    update_timestamp = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=1000, blank=True, null=True)
    updated_by = models.CharField(max_length=1000, blank=True, null=True)
    

    class Meta:
        managed = False
        db_table = 'OFCOM_DIAL_CODE'


class DcmFileAuditStatusLog(models.Model):
    id = models.FloatField(primary_key=True)
    file_id = models.CharField(max_length=1000, blank=True, null=True)
    file_name = models.CharField(max_length=1000, blank=True, null=True)
    file_type = models.CharField(max_length=1000, blank=True, null=True)
    number_type = models.CharField(max_length=1000, blank=True, null=True)
    destination = models.CharField(max_length=1000, blank=True, null=True)
    process_config_id = models.FloatField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=1000, blank=True, null=True)
    error = models.CharField(max_length=1000, blank=True, null=True)
    record_count = models.FloatField(blank=True, null=True)
    record_failed = models.FloatField(blank=True, null=True)
    record_pass = models.FloatField(blank=True, null=True)
    record_pass_warning = models.FloatField(blank=True, null=True)
    file_extn = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DCM_FILE_AUDIT_STATUS_LOG'