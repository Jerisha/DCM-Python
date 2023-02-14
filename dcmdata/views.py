from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from .serializers import *
#from  rest_framework_simplejwt.views import TokenViewBase
from django.conf import settings
from . import getmethods
from .export_to_csv import *
import traceback
import json5

 

#For User

 

class QueryObjectView(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self, request, format=None):
        error_file=open("error_log.txt","w")
        response_type ="QUERY"
        error_msg = 'No Error Found'
        status = 'SUCCESS'
        status_code = 'PY1000'
        number_range = ""
        number_range_type = ""
        data = []
        dcm_count = 0
        username = ''
        report_identifier = ''
        sub_report_name = ''
        profile_name = ''
        final_response = {}
        number_range_list = ['GEO','INT','NGN','OFCOM']
        export_flag='N'
        export_sql = ""
        try:
            req = request.data
            str_req=req
            error_file.write("\n"+str(req))
            if "UserParams" in req:
                username = req["UserParams"][0]["UserID"]
            if "RequestParams" in req:
                report_identifier = req["RequestParams"][0]["ReportIdenitifer"]
                export_flag=req["RequestParams"][0]["IsExportToExcel"]
                pagenumber = req['RequestParams'][0]['PageNumber']

            sub_report_name = report_identifier

            if report_identifier == "SearchViewExtract":
                number_range = ""
                number_range_operator = ""
                number_range_type = ""
                print(req['Data'][0]['number_range'])
                try:
                    if "number_range" in req['Data'][0]: 
                        number_range = req['Data'][0]['number_range']
                        
                except:
                    pass
                if "number_range_operator" in req['Data'][0]: 
                    number_range_operator = req['Data'][0]['number_range_operator']
                    error_file.write("\nNumber Range Operator"+number_range_operator)
                if "number_range_type" in req['Data'][0]: 
                    number_range_type = req['Data'][0]['number_range_type']

                #error_file.write("\nnumber_range -->"+str(number_range)+" number_range_type -->"+str(number_range_type))


                if number_range_type not in number_range_list:
                    error_msg = 'Number Range Type Not Found'
                    status_code='PY2000'
                    raise Exception(error_msg)
                start = 0
                end = 500
                if pagenumber > 1 : 
                    start = (500 * (pagenumber-1))
                    end = start + 500
                #final_data = data[start:end]
                
                returnedData = getmethods.search_dcm(number_range,number_range_operator,number_range_type, start, end)

                
                if returnedData != {}:
                    
                    dcm_count = returnedData.get("dcm_count")
                    data = returnedData.get("dcm_data")
                    export_sql=returnedData.get("export_sql")
                    error_file.write("\nData List:"+str(export_sql))
                    """if(export_flag=='Y'):
                        DataExporter(report_identifier, username, str(returnedData[2]))"""


                if(export_flag=='Y' and dcm_count>0):
                    exportResponse =  DataExporter(report_identifier, username, str(export_sql))
                    DataExport=open("DataExportLog.csv","w")
                    DataExport.write(str(exportResponse))
                    return exportResponse
                else:
                    final_response = {
                    "Response": response_type,
                    "Status": [
                        {
                            "StatusCode": status_code,
                            "StatusMessage": status,
                            "MessageType": "Informational"
                        }
                    ],
                    "ReponseParams": {
                        "ReportIdenitifer":report_identifier,
                        "SubReportName": sub_report_name,
                        "UserId": username,
                        "RecordIdentifier":report_identifier,
                        "RecordCount":dcm_count,
                    },
                    "Data": data,
                    "error": error_msg
                    }

                    if sub_report_name == "UserProfile": 
                        final_response['ReponseParams'].update({"ProfileName" : profile_name})

                    
                    #error_file.close()
             
                    #return JsonResponse(final_response, safe=False)

            elif  report_identifier == "AuditTableView":
                audit_count=0
                data=[]

                file_name = ""
                file_name_operator = ""
                file_type=""
                #file_type_operator=""
                number_type=""
                #source_operator=""
                destination=""
                #destination_operator=""
                try:
                    if "file_name" in req['Data'][0]: 
                        file_name = req['Data'][0]['file_name']
                        
                except:
                    pass
                if "file_name_operator" in req['Data'][0]: 
                    file_name_operator = req['Data'][0]['file_name_operator']
                    #error_file.write("\nFile ID Operator"+file_id_operator)

                if "file_type" in req['Data'][0]: 
                    file_type = req['Data'][0]['file_type']

                if "number_type" in req['Data'][0]: 
                    number_type = req['Data'][0]['number_type']

                if "destination" in req['Data'][0]: 
                    destination = req['Data'][0]['destination']

                start = 0
                end = 500
                if pagenumber > 1 : 
                    start = (500 * (pagenumber-1))
                    end = start + 500
                #final_data = data[start:end]
                
                returnedData = getmethods.search_audit(file_name,file_name_operator, file_type, number_type, destination, start, end)  

                if returnedData != {}:
                    
                    audit_count = returnedData.get("audit_count")
                    data = returnedData.get("audit_data")

                final_response = {
                    "Response": response_type,
                    "Status": [
                        {
                            "StatusCode": status_code,
                            "StatusMessage": status,
                            "MessageType": "Informational"
                        }
                    ],
                    "ReponseParams": {
                        "ReportIdenitifer":report_identifier,
                        "SubReportName": sub_report_name,
                        "UserId": username,
                        "RecordIdentifier":report_identifier,
                        "RecordCount":audit_count,
                    },
                    "Data": data,
                    "error": error_msg
                    }

                if sub_report_name == "UserProfile": 
                    final_response['ReponseParams'].update({"ProfileName" : profile_name})

                     

        except Exception as e:
            error_file.write("\nerror:"+str(e))
            error_file.write("\nError:"+traceback.format_exc())
            error_msg = e
            status = 'FAILURE'
            if status_code!='PY2000':
                status_code='PY3000'

            final_response = {
            "Response": response_type,
            "Status": [
                {
                    "StatusCode": status_code,
                    "StatusMessage": status,
                    "MessageType": "Informational"
                }
            ],
            "ReponseParams": {
                "ReportIdenitifer":report_identifier,
                "SubReportName": sub_report_name,
                "UserId": username,
                "RecordIdentifier":report_identifier,
		        "RecordCount":dcm_count,
            },
            "Data": data,
            "error": error_msg
            }
            if sub_report_name == "UserProfile": 
                final_response['ReponseParams'].update({"ProfileName" : profile_name})
            
            #error_file.write("\n"+str(final_response))
        error_file.write("\n\n\FINAL RESPONSE:"+str(final_response))
        error_file.close()

        return JsonResponse(final_response, safe=False)
        
