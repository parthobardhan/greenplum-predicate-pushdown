import os
import cx_Oracle
from os import environ
connection = cx_Oracle.connect("oraadmin", "oraadmin1234", "oracledb.c85pu3q6udi4.us-east-2.rds.amazonaws.com/ORCL")
cursor = connection.cursor()
if environ.get('QUERYFILTER') is not None:
        querystring= "select * from TEST where " + environ.get('QUERYFILTER')
else:
        querystring = "select * from TEST"
cursor.execute(querystring)
result=cursor.fetchall()
for row in result:
        if row is None:
                print ''
        print row[0],'|',row[1]
connection.close()
