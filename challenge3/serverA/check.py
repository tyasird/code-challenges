import mysql.connector
import os

try:
    cnx = mysql.connector.connect(user='user', password='password', host='db')
    if (cnx.connection_id):
        print(f'********* ServerA -> DB: mysql connection is OK. *********')
        print(cnx.cmd_statistics())
    cnx.close()
except Exception as e:
    print(e)
    print('********* ServerA Could not connect to mysql *********')



