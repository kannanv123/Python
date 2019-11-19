import mysql.connector
import csv

mydb = mysql.connector.connect(
  host="localhost",
  user="kannanv",
  passwd="V@mstiU1Md",
  database="sbn_aws_test1"
)
mycursor = mydb.cursor()
try:
     mycursor.execute("SELECT * FROM aws_inventory")
     myresult = mycursor.fetchall()
     for x in myresult:
         print(x)
except IndexError:
  print("ioeror")

