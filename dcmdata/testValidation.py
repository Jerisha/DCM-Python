import cx_Oracle
#from django.db import connection as con

con=cx_Oracle.connect(user='osnmgr', password='osnmgru1dx', dsn='osn2ud1-db.ad.plc.cwintra.com/osn2ud1' )
dbCount = "select count(*) from STG_DCM_INT"

cursor=con.cursor()
cursor.execute(dbCount)
queryCount = cursor.fetchone()
getDbCountError.write("\nQUERY_COUNT:"+str(queryCount))
con.close()
getDbCountError.close()

print("Number of files present in DB:-", queryCount[0])

#Setting initial value of the counter to zero
rowCount  = 0
#iterating through the whole file
for row in open("INT sample data.csv"):
  rowCount+= 1
 #printing the result
print("Number of lines present in CSV File:-", rowCount)

if(queryCount[0] == rowCount):
    print("All Good!")
else:
    print("All Not Good")