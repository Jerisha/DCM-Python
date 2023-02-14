from .models import *
from rest_framework import serializers



class SearchDCMSerializer(serializers.ModelSerializer):
    class Meta:
        model = DcmDialCode
        exclude=["number_range_skey","insert_timestamp","update_timestamp","created_by","updated_by","current_flag"] 
		
class SearchDCMOffcomSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfcomDialCode
        exclude=["number_range_skey"]

class SearchDCMAuditSerializer(serializers.ModelSerializer):
    class Meta:
        model = DcmFileAuditStatusLog
        fields = '__all__'

