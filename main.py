import mysql.connector as msc
from  password import pwd
mydb = msc.connector.connect(
  host="localhost",
  user="root",
  password=pwd,
  database="dhaage"
)

print(mydb)
