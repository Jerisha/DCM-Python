import cx_Oracle
import traceback
from django.db import connection as con

#connector=cx_Oracle.connect(user='osnmgr', password='osnmgru1dx', dsn='osn2ud1-db.ad.plc.cwintra.com/osn2ud1' )

def getQueryCount(sqlQueryCount):

    getDbCountError=open("GetDbCountError.txt",'w')

    try:

        #con=connector

        cursor=con.cursor()
        cursor.execute(sqlQueryCount)
        queryCount = cursor.fetchone()
        getDbCountError.write("\nQUERY_COUNT:"+str(queryCount))
        con.close()
        getDbCountError.close()
        
        return queryCount[0]

        

    except Exception as e:
	    getDbCountError.write("\nError:"+traceback.format_exc())

    
    
