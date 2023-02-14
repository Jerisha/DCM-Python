from .serializers import *
from .models import *
from . import getDbCount
import traceback
#import serializers
#import models

def search_dcm(number_range, number_range_operator, number_range_type, start, end):
	export_sql = ""
	dcm_data = {}
	dcm_count = 0
	get_methods_error=open("get_methods_error.txt","w")
	number_range_type = number_range_type.upper()
	try:
	
		get_methods_error.write("In GET METHODS")
	
		where_con=""
        	#print(number_range,number_range_type)
	
	
	 
		if number_range_type == "GEO" or number_range_type == "INT" or number_range_type=="NGN":
			if number_range !="":
				get_methods_error.write("number_range")
				if(number_range_operator=="like"):
					where_con=" and t.number_range like '"+str(number_range)+"%%'"
				elif(number_range_operator=="equal"):
					where_con=" and t.number_range = '"+str(number_range)+"'"
				get_methods_error.write(where_con)
			else:
				where_con=""

	
			sql_query="select m.* from \
			(select t.*, row_number() over (order by t.number_range) as rn from DCM_DIAL_CODE t where upper(t.number_range_type)= '"+number_range_type+"'"+where_con+") m \
			 where rn>"+str(start)+" and rn<="+str(end)+" order by rn" 
			get_methods_error.write(sql_query)
			
			sqlQueryCount="select count(*) as dcmcount from DCM_DIAL_CODE t where upper(t.number_range_type)= '"+number_range_type+"'"+where_con

			export_sql="select t.*, row_number() over (order by t.number_range) as rn from DCM_DIAL_CODE t where upper(t.number_range_type)= '"+number_range_type+"'"+where_con

			dcm_data = DcmDialCode.objects.raw(sql_query)
			dcm_count = getDbCount.getQueryCount(sqlQueryCount)
			get_methods_error.write("\n******"+str(sql_query)+"*************\n")
			get_methods_error.write("\n"+str(len(dcm_data))+"\n")
			serializer = SearchDCMSerializer(dcm_data, many = True)
			dcm_data = serializer.data
			get_methods_error.write("\n"+str(len(dcm_data))+"\n")
			
		elif number_range_type == "OFCOM":
			if number_range !="":
				get_methods_error.write("number_range")
				if(number_range_operator=="like"):
					where_con=" where t.number_block like '"+str(number_range)+"%%'"
				elif(number_range_operator=="equal"):
					where_con=" where t.number_block = '"+str(number_range)+"'"
				get_methods_error.write(where_con)
			else:
				where_con=""

			sql_query="select m.* from \
			(select t.*, row_number() over (order by t.number_block) as rn from OFCOM_DIAL_CODE t"+where_con+") m \
			where rn>"+str(start)+" and rn<="+str(end)+" order by rn"
			get_methods_error.write(sql_query)
			sqlQueryCount="select count(*) as dcmcount from OFCOM_DIAL_CODE t"+where_con
			get_methods_error.write("\n******"+str(sql_query)+"*************\n")
			get_methods_error.write("\n******"+str(sqlQueryCount)+"*************\n")

			export_sql="select t.* from OFCOM_DIAL_CODE t "+where_con
			try:
				dcm_data = OfcomDialCode.objects.raw(sql_query)
			except Exception as e:
				get_methods_error.write(str(e))
			dcm_count = getDbCount.getQueryCount(sqlQueryCount)
			#get_methods_error.write(str(dcm_count))
			get_methods_error.write("\ndcm_datacount"+str(len(dcm_data)))
			serializer = SearchDCMOffcomSerializer(dcm_data, many = True)
			dcm_data = serializer.data

			
		get_methods_error.write("\n****DCM_COUNT***:"+str(dcm_count))
	

		if len(dcm_data) == 0:
			final_respone = {}
			return final_respone
		
	except Exception as e:
		get_methods_error.write("\nError:"+traceback.format_exc())

	get_methods_error.write("\nEXPORT:"+str(export_sql))
	get_methods_error.close()

	return_response={
		"dcm_data": dcm_data,
		"dcm_count": dcm_count,
		"export_sql": str(export_sql)  
	}

	return return_response	
	#return [dcm_data, dcm_count, str(export_sql)]

def search_audit(file_name,file_name_operator, file_type, source, destination, start, end):
	audit_data = {}
	audit_count = 0
	return_response = {}
	where_con=" where t.id <> 1"
	get_methods_error=open("get_methods_error.txt","w")
	try:
		if file_name !="":
			get_methods_error.write("file_name")
			if(file_name_operator=="like"):
				where_con=where_con+" and upper(t.file_name) like '%%"+str(file_name.upper())+"%%'"
			elif(file_name_operator=="equal"):
				where_con=where_con+" and upper(t.file_name) = '"+str(file_name.upper())+"'"
			get_methods_error.write(where_con)
		
		if file_type !="":
			get_methods_error.write("file_type")
			where_con=where_con+" and upper(t.file_type) = '"+str(file_type.upper())+"'"
			get_methods_error.write(where_con)

		if source !="":
			get_methods_error.write("source")
			where_con=where_con+" and upper(t.source) = '"+str(source.upper())+"'"
			get_methods_error.write(where_con)

		if destination !="":
			get_methods_error.write("destination")
			where_con=where_con+" and upper(t.destination) = '"+str(destination.upper())+"'"
			get_methods_error.write(where_con)


		audit_query="select m.* from \
		(select t.*, row_number() over (order by t.start_time desc) as rn from DCM_FILE_AUDIT_STATUS_LOG t"+where_con+") m \
		where rn>"+str(start)+" and rn<="+str(end)+" order by rn"
		auditQueryCount="select count(*) as auditcount from DCM_FILE_AUDIT_STATUS_LOG t"+where_con
		get_methods_error.write("\n******"+str(audit_query)+"*************\n")
		get_methods_error.write("\n******"+str(auditQueryCount)+"*************\n")

		audit_data = DcmFileAuditStatusLog.objects.raw(audit_query)
		audit_count = getDbCount.getQueryCount(auditQueryCount)
		get_methods_error.write("\n******"+str(audit_query)+" AUDIT QUERY*************\n")
		get_methods_error.write("\n"+str(len(audit_data))+"\n")
		serializer = SearchDCMAuditSerializer(audit_data, many = True)
		audit_data = serializer.data
		get_methods_error.write("\n"+str(len(audit_data))+"\n")

		if len(audit_data) == 0:
				final_respone = {}
				return final_respone
			
		#except Exception as e:
			#get_methods_error.write("\nError:"+traceback.format_exc())

		get_methods_error.close()

		return_response={
			"audit_data": audit_data,
			"audit_count": audit_count
		}
	except Exception as e:
		get_methods_error.write("\nError:"+traceback.format_exc())


	return return_response
