from django.db import connection as con
import csv
import sys, os
from datetime import datetime
from django.http import FileResponse

def DataExporter(reportIdentifier, userName, sqlQuery):

    export_error_log=open("export_error_log.txt","w")
    export_error_log.write(sqlQuery)
    export_path="/opt/SP/osnapp/dcmadmin/excel/"

    #con=connector
    cursor=con.cursor()

    currentTime=datetime.now()
    currentTimeStr=currentTime.strftime("%d%m%Y%H%M%S")
    fileName=reportIdentifier+"_"+userName+"_"+currentTimeStr+".csv"
    filePath=export_path+fileName
    csv_file = open(filePath, "w")
    writer = csv.writer(csv_file, delimiter=',', lineterminator="\n", quoting=csv.QUOTE_NONNUMERIC)

    cursor.execute(sqlQuery)

    table_export = cursor.fetchall()
    writer.writerow(i[0] for i in cursor.description)

    for row in table_export:
        writer.writerow(row)

    csv_file.close()
    
    returnFile = open(filePath, 'rb')
    response = FileResponse(returnFile)
    response['Content-Type'] = 'application/octet-stream'
    export_error_log.write("\n export response     "+str(response)+"   ***********")

    con.close()

    return response
