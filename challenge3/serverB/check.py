import mysql.connector
import os

hostname = "servera" 
response = os.system("ping -c 1 " + hostname)
if response == 0:
  print (f'*********ServerB ping:{hostname} is UP!*********')
else:
  print (f'*********ServerB ping:{hostname} is DOWN!*********')

